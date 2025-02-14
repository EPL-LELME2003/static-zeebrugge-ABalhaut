#Augustin Balhaut 34282100
import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()

# Define model parameters
Vboat = 200000
LHV_CH4 = 50 * 10**6
rho_CH4 = 500
losses_CH4 = 0.35
H2t_CH4 = 0.25

LHV_NH3 = 18.5 * 10**6
rho_NH3 = 600
losses_NH3 = 0.4
H2t_NH3 = 0.18

CO2CH4 = 2.75

# Define model variables
model.boatsCH4 = pyo.Var(within = pyo.NonNegativeReals, bounds =(0,100)) 
model.boatsNH3 = pyo.Var(within = pyo.NonNegativeReals, bounds =(0,100))


# Define the objective functions
model.obj = pyo.Objective(expr = Vboat*rho_CH4*H2t_CH4*model.boatsCH4 + Vboat*rho_NH3*H2t_NH3*model.boatsNH3, sense = pyo.maximize)



# Define the constraints
def con_rule1(model):
    return model.boatsCH4 + model.boatsNH3 <= 100
model.con = pyo.Constraint(rule = con_rule1)

def con_rule2(model):
    return Vboat*rho_CH4*model.boatsCH4*CO2CH4 <= 14*10**6
model.con2 = pyo.Constraint(rule = con_rule2)

def con_rule3(model):
    return Vboat*rho_CH4*model.boatCH4*LHV_CH4/(1-losses_CH4) + Vboat*rho_NH3*model.boatsNH3*LHV_NH3/(1-losses_NH3) <= 140*10**12
model.con3 = pyo.Constraint(rule = con_rule3)


# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('...')
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
