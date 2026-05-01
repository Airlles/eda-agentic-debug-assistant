
# EDA Debug Report

## Likely Issue Type
UNCONNECTED_NET

## Evidence From Log

### Errors
['Error: Signal data_valid is undriven and has no source driver', 'Info: Elaboration completed with warnings and errors']

### Warnings
['Warning: Net temp_result is declared but never driven', 'Warning: Output port done is unconnected in instance u_controller']

## Retrieved Debug Context
UNCONNECTED_NET

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


## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
