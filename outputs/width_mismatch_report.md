
# EDA Debug Report

## Likely Issue Type
WIDTH_MISMATCH

## Evidence From Log

### Errors
['Error: Port data_in of module alu_core expects 8 bits but connected signal sw_input has 4 bits', 'Info: Compilation stopped due to errors']

### Warnings
['Warning: Width mismatch in assignment at alu.v line 24', 'Warning: Signal result expects 8 bits but expression provides 4 bits']

## Retrieved Debug Context
WIDTH_MISMATCH

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


## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
