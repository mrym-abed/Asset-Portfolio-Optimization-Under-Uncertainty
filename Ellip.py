import pyomo.environ as pyo  

# Define the model  
model = pyo.ConcreteModel()  

# Define the set of indices  
model.iset = pyo.Set(initialize=range(1, 11))  

# Define the parameter 'k'  
model.k = pyo.Param(initialize=4) 

# Define the data dictionaries  
data_L = {1: 0.01, 2: 0.01, 3: 0.01, 4: 0.01, 5: 0.01, 6: 0.01, 7: 0.01, 8: 0.01, 9: 0.01, 10: 0.01} 
data_U = {1: 0.5, 2: 0.5, 3: 0.5, 4: 0.5, 5: 0.5, 6: 0.5, 7: 0.5, 8: 0.5, 9: 0.5, 10: 0.5}
data_mean_hat = {1: 0.0667, 2: 0.0667, 3: 0, 4: 0, 5: -0.0267, 6: 0.0333, 7: 0.0333, 8: -0.0833, 9: 0.0333, 10: 0.01}
data_stv = {1: 0.4784, 2: 0.0089, 3: 0.02, 4: 0.0233, 5: 0.0169, 6: 0.089, 7: 0.0133, 8: 0.0011, 9: 0.2433, 10: 0}

# Define the parameters  
model.L = pyo.Param(model.iset, initialize=data_L)  
model.U = pyo.Param(model.iset, initialize=data_U)  
model.mean_hat = pyo.Param(model.iset, initialize=data_mean_hat)  
model.stv = pyo.Param(model.iset, initialize=data_stv)  

# Define the decision variables  
model.x = pyo.Var(model.iset, domain=pyo.NonNegativeReals)  
model.u = pyo.Var(model.iset, domain=pyo.Binary)  
model.W = pyo.Var(domain=pyo.Reals)  # Objective variable  

# Define the objective function  
def rule_obj(model):  
    return model.W  

model.obj = pyo.Objective(rule=rule_obj, sense=pyo.maximize)  

# Define the constraints  
def rule_const1(model):  
    return sum(model.u[i] for i in model.iset) == model.k  
model.const1 = pyo.Constraint(rule=rule_const1)  

def rule_const2(model):  
    return sum(model.x[i] for i in model.iset) == 1  
model.const2 = pyo.Constraint(rule=rule_const2)  

model.const3 = pyo.ConstraintList()  
for i in model.iset:  
 model.const3.add(model.x[i] <= model.U[i] * model.u[i])
 model.const3.add(model.x[i] >= model.L[i] * model.u[i])

def rule_const4(model):  
    return (  
        model.W - sum(model.mean_hat[i] * model.x[i] for i in model.iset) +   
        ((sum((model.stv[i] * model.x[i])**2 for i in model.iset))**(1/2)) <= 0  
    )

model.const4 = pyo.Constraint(rule=rule_const4)  

# Solve the optimization problem  
solver = pyo.SolverFactory('gams')  
results = solver.solve(model, tee=True, add_options=["option optcr=0;"])

# Check if the solver found an optimal solution  
if results.solver.termination_condition == pyo.TerminationCondition.optimal:  
    # Print the optimal solution  
    print('Optimal Objective Value:', pyo.value(model.obj))  
    print('Optimal Solution:')  
    for i in model.iset:  
        print(f'x[{i}] = {pyo.value(model.x[i])}')  
        print(f'u[{i}] = {pyo.value(model.u[i])}')  
        optimal_return = sum(pyo.value(model.x[i]) * pyo.value(model.mean_hat[i]) for i in model.iset)  
    print('Optimal return:', optimal_return)  
else:  
    print('No optimal solution found. Solver status:', results.solver.status)  
    print('Solver termination condition:', results.solver.termination_condition)  