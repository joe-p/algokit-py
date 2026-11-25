# 2.2.1-beta.3 - October 13th, 2026

# 2.2.0 - July 24th, 2025

## Features

- Add support for generating a minimal client ([#76](https://github.com/algorandfoundation/algokit-client-generator-py/issues/76))

# 2.1.0 - March 26th, 2025

## Features

- Bump utils dependency to v4

# 2.0.1 - March 13th, 2025

## Fixes

- Ensure close_out calls are generated in composer ([#54](https://github.com/algorandfoundation/algokit-client-generator-py/issues/54))

# 2.0.0 - February 18th, 2025

## Breaking Changes

- Generator overhaul with ARC-56 support and TypeScript alignment

## Features

- V2 - leveraging new AlgoKit interfaces and support for algokit-utils-py v3 ([#33](https://github.com/algorandfoundation/algokit-client-generator-py/issues/33))

## Fixes

- Update to latest utils to fix state key name normalization issues similarly to utils-ts ([#43](https://github.com/algorandfoundation/algokit-client-generator-py/issues/43))
- Correcting the ignore declaration for a more appropriate mypy global ignore ([#41](https://github.com/algorandfoundation/algokit-client-generator-py/issues/41))
- Disable mypy for end user; keep selective ignores for local examples ([#40](https://github.com/algorandfoundation/algokit-client-generator-py/issues/40))
- Minor patches in dataclass inheritance; fixes for mypy errors; addressing internal feedback ([#37](https://github.com/algorandfoundation/algokit-client-generator-py/issues/37))
- Ensure nested dataclasses in state accessors are loaded properly ([#36](https://github.com/algorandfoundation/algokit-client-generator-py/issues/36))
- Extra section in migration for state access; adding @property decorator for direct state access ([#35](https://github.com/algorandfoundation/algokit-client-generator-py/issues/35))

# 1.1.7 - August 8th, 2024

# 1.1.6 - August 1st, 2024

## Fixes

- Additional changes to address mypy 'call-overload'; adding cron for ci ([#29](https://github.com/algorandfoundation/algokit-client-generator-py/issues/29))
- Addressing mypy 'call-overload' warning with explicit typecast ([#28](https://github.com/algorandfoundation/algokit-client-generator-py/issues/28))

# 1.1.5 - June 13th, 2024

## Fixes

- Set explicit utf-8 encoding as part of writer invocation ([#27](https://github.com/algorandfoundation/algokit-client-generator-py/issues/27))

# 1.1.4 - May 13th, 2024

## Fixes

- Ensure clients generated for contracts with no abi methods are still valid python

# 1.1.3 - March 27th, 2024

# 1.1.2 - February 6th, 2024

# 1.1.1 - January 8th, 2024

# 1.1.0 - December 14th, 2023

## Features

- Add support for simulating an atc ([#17](https://github.com/algorandfoundation/algokit-client-generator-py/issues/17))

## Fixes

- Adjust client tests ([#18](https://github.com/algorandfoundation/algokit-client-generator-py/issues/18))

# 1.0.3 - October 17th, 2023

# 1.0.2 - June 23rd, 2023

## Fixes

- Fix account reference types ([#13](https://github.com/algorandfoundation/algokit-client-generator-py/issues/13))

# 1.0.1 - June 13th, 2023

## Fixes

- Add support for reference type aliases ([#12](https://github.com/algorandfoundation/algokit-client-generator-py/issues/12))

# 1.0.0 - June 6th, 2023

## Breaking Changes

- Initial release ([#11](https://github.com/algorandfoundation/algokit-client-generator-py/issues/11))

# 0.1.0 - June 6th, 2023

## Features

- Add compose functionality to generated clients ([#9](https://github.com/algorandfoundation/algokit-client-generator-py/issues/9))
- Add additional doc strings
- Generate client method docstrings
- Expand supported types
- Forward commonly used properties
- Support for named structs
- Convert special methods from overloads to prefixed names
- Improve CLI parsing robustness
- Enable running as a CLI
- Add algokit typed client generator

## Fixes

- Use logger instead of print
- Remove GenerationSettings
- Reduce type warnings
- Use names derived from ABI signature if overloads
- Rename CLI alias to algokitgen-py
- Map byte[] to bytes ([#3](https://github.com/algorandfoundation/algokit-client-generator-py/issues/3))
