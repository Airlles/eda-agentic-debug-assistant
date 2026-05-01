
# EDA Debug Report

## Likely Issue Type
TIMING_VIOLATION

## Evidence From Log

### Errors
['Error: Setup slack is negative on path from reg_a to reg_b', 'Error: Worst negative slack: -1.245 ns']

### Warnings
['Warning: Timing violation detected on clock clk']

## Retrieved Debug Context
TIMING_VIOLATION

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


## Suggested Next Steps
1. Inspect the error and warning lines shown above.
2. Open the RTL file mentioned in the log.
3. Compare the signal declarations and module port connections.
4. Fix one issue at a time, then rerun synthesis or simulation.
