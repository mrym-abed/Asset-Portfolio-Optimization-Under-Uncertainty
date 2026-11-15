import pyomo.environ as pyo  

# Define the model  
model = pyo.ConcreteModel()  

# Define the set of indices  
model.iset = pyo.Set(initialize=range(1, 21))  

# Define the parameter 'k'  
model.k = pyo.Param(initialize=5) 

# Define the data dictionaries  
data_L = {i:0.01  for i in model.iset} 
data_U = {i:0.3  for i in model.iset} 
data_mean_hat = {1: 0.001093864, 2: 0.0000143073, 3: 0.0000148, 4: 0.001072744, 5: 0.00869, 6: 0.000911759, 7: 0.000998716, 8: 0.002109282, 9: 0.002129664, 10: 0.00210928, 
     11: 0.001759014, 12: -0.002383711, 13: 0.000158623, 14: 0.000919638, 15: 0.001578623, 16: 0.000720149, 17: 0.000889186, 18: -0.000942714, 19: 0.00518493, 20: 0.000416}

data_stv = {1: 0.000449132, 2: 0.00429, 3: 0.003950798, 4: 0.000372, 5: 0.014055357, 6: 0.000389, 7: 0.000365, 8: 0.017387915, 9: 0.0186, 10: 0.015778975
, 11: 0.014072387, 12: 0.0509, 13: 0.0152, 14: 0.013773591, 15: 0.00935, 16: 0.010940771, 17: 0.006201908, 18: 0.026530891, 19: 0.00849, 20: 0.00574
}

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
    return model.W - sum(model.mean_hat[i] * model.x[i] for i in model.iset) + \
           sum(model.stv[i] * model.x[i] for i in model.iset) <= 0  

model.const4 = pyo.Constraint(rule=rule_const4)  

# Solve the optimization problem  
solver = pyo.SolverFactory('gams')  
results = solver.solve(model, tee=True)  

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