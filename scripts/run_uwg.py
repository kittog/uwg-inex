# import modules
from uwg import UWG # urban weather generator

# define epw file path
epw_path = "path/to/epw" 

# intialize UWG model by passing arguments or relying on default values
model = UWG.from_param_args(epw_path=epw_path, bldheight=10, blddensity=0.5,
                            vertohor=0.8, grasscover=0.1, treecover=0.1, zone='1A')

model.generate() # generate model
model.simulate() # run simulation

# write the simulation result to a file
# by default, will add "_UWG" suffix to filename
model.write_epw()