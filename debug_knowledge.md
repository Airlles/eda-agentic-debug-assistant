# RTL and EDA Debug Knowledge Base

## WIDTH_MISMATCH

A width mismatch happens when two signals with different bit widths are connected or assigned.

Common causes:
1. A module port expects a wider or narrower signal than the one connected to it.
2. A wire or reg declaration has the wrong vector range.
3. A bus slice selects the wrong number of bits.
4. An assign statement connects incompatible signal widths.

Debug steps:
1. Check the module port declaration.
2. Check the connected signal declaration.
3. Compare the left side and right side of the assignment.
4. Look for missing vector ranges such as [7:0].
5. Inspect module instantiations for incorrect port connections.

Files to inspect:
1. Verilog source files
2. Module instantiation files
3. Top level RTL file


## MISSING_MODULE

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


## TIMING_VIOLATION

A timing violation happens when a signal path is too slow for the required clock period.

Common causes:
1. Too much combinational logic exists between registers.
2. The clock period constraint is too aggressive.
3. A long routing path increases delay.
4. Register placement causes excessive path delay.

Debug steps:
1. Check the timing report.
2. Identify the failing path.
3. Look at setup slack or hold slack.
4. Reduce combinational logic depth.
5. Add pipeline registers if needed.
6. Check clock constraints.

Files to inspect:
1. Timing report
2. Constraints file
3. RTL datapath modules


## UNCONNECTED_NET

An unconnected net happens when a signal is declared but not driven, not used, or not connected to a module port.

Common causes:
1. A wire is declared but never assigned.
2. A module port is left disconnected.
3. A typo creates a new unintended signal.
4. An output is not driven by any logic.

Debug steps:
1. Search for the signal name in the RTL.
2. Check whether the signal is assigned.
3. Check module port connections.
4. Look for spelling mistakes.
5. Confirm that every output has a driver.

Files to inspect:
1. RTL source files
2. Top level module
3. Module instantiations


## SYNTAX_ERROR

A syntax error happens when the HDL compiler cannot parse the Verilog code.

Common causes:
1. Missing semicolon.
2. Missing endmodule.
3. Incorrect always block syntax.
4. Mismatched parentheses or brackets.
5. Invalid keyword usage.

Debug steps:
1. Go to the line number shown in the log.
2. Check the line before the reported error.
3. Look for missing semicolons.
4. Check module, always, if, case, and end statements.
5. Recompile after fixing one syntax issue at a time.

Files to inspect:
1. Verilog source file mentioned in the error
2. Nearby lines before the reported error

