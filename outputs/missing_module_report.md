
# EDA Debug Report

## Likely Issue Type
MISSING_MODULE

## Evidence From Log

### Errors
['Error: Module not found: alu_core', 'Error: Cannot find module definition for instance u_alu']

### Warnings
['Warning: Design unit top_module depends on missing module alu_core']

## Retrieved Debug Context
MISSING_MODULE

A missing module error happens when the compiler or simulator cannot find the Verilog definition for an instantiated module.

Common causes:
1. The source file was not added to the project.
2. The module name in the file does not match the instantiated name.
3. The file path is incorrect.
4. The compile order is wrong.

Debug steps:
1. Check that the module source file exists.
2. Check that the module name matches the instantiation.
3. Add the missing file to the Quartus or ModelSim project.
4. Recompile all source files.
5. Check compile order if using simulation scripts.

Files to inspect:
1. Project source file list
2. Verilog module files
3. Simulation compile script


## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
