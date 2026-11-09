# 4.2.4-beta.4 - August 14th, 2026

## Fixes

- Avoid error transformer app id prefix collisions ([#325](https://github.com/algorandfoundation/algokit-utils-py/pull/325))
- Stringify JS-unsafe integers in AVM simulation traces ([#324](https://github.com/algorandfoundation/algokit-utils-py/pull/324))

# 4.2.3 - December 15th, 2025

## Fixes

- Update urllib3 for audit issue ([#239](https://github.com/algorandfoundation/algokit-utils-py/issues/239))
- Enable LocalNet dispensing after 30000 rounds ([#226](https://github.com/algorandfoundation/algokit-utils-py/issues/226))
- Use extra pages available when deploying ([#217](https://github.com/algorandfoundation/algokit-utils-py/issues/217))

# 4.2.2 - October 15th, 2025

## Fixes

- Extract pc from simulation trace for rejected transactions during simulation
- Add app id first when populating a box ref

# 4.2.1 - September 19th, 2025

## Fixes

- Allow simulating with empty signatures like TS supports ([#196](https://github.com/algorandfoundation/algokit-utils-py/issues/196))
- Support for 4.3.0 go algorand access lists feature

# 4.2.0 - August 11th, 2025

## Features

- Error transformers feature parity with utils-ts ([#186](https://github.com/algorandfoundation/algokit-utils-py/issues/186))

# 4.1.0 - June 19th, 2025

## Features

- Send payment transaction with algokit core
- Calculated fee using assign_fee from core
- Using AlgodApi OpenAPI generated client to send transactions to a node
- Using AlgoKit Core to build a payment transaction

## Fixes

- Remove prepending the prefix twice ([#154](https://github.com/algorandfoundation/algokit-utils-py/issues/154))
- Readonly simulate extra opcode budget handling ([#180](https://github.com/algorandfoundation/algokit-utils-py/issues/180))
- Fixes ABI return handling for bare create/delete ([#178](https://github.com/algorandfoundation/algokit-utils-py/issues/178))
- Pip-audit failure for setuptools
- Deployment send params aren't passed into the composer
- Correctly re-throw the exception
- Introducing tagged releases for the integration with algokit-core
- Keep the user min fee if set

# 4.0.1 - May 1st, 2025

## Fixes

- Bumps httpx dependency for compatibility ([#152](https://github.com/algorandfoundation/algokit-utils-py/issues/152))

# 4.0.0 - March 26th, 2025

## Breaking Changes

- Enable resource population by default ([#151](https://github.com/algorandfoundation/algokit-utils-py/issues/151))

## Features

- Enable resource population by default ([#151](https://github.com/algorandfoundation/algokit-utils-py/issues/151))

# 3.0.2 - February 22nd, 2025

## Fixes

- Correctly return group id when resource population is enabled ([#145](https://github.com/algorandfoundation/algokit-utils-py/issues/145))

# 3.0.1 - February 19th, 2025

## Fixes

- Minor deploy behaviour and logger instantiation patches ([#143](https://github.com/algorandfoundation/algokit-utils-py/issues/143))

# 3.0.0 - February 18th, 2025

## Breaking Changes

- Major restructuring and new app client interfaces

## Features

- Algokit-utils-py v3 implementation ([#119](https://github.com/algorandfoundation/algokit-utils-py/issues/119))

## Fixes

- Remove deprecation decorator causing side effects ([#141](https://github.com/algorandfoundation/algokit-utils-py/issues/141))
- Name normalization in arc56 contract; extra test for more verbose validation ([#140](https://github.com/algorandfoundation/algokit-utils-py/issues/140))
- Addressing internal feedback (batch 6) ([#139](https://github.com/algorandfoundation/algokit-utils-py/issues/139))
- Expose algosdk lsig, multisig object instances in account wrappers ([#138](https://github.com/algorandfoundation/algokit-utils-py/issues/138))
- Feedback batch #4 ([#136](https://github.com/algorandfoundation/algokit-utils-py/issues/136))
- Detect changes in extra program pages as a schema break ([#135](https://github.com/algorandfoundation/algokit-utils-py/issues/135))
- Addressing internal feedback (3) ([#134](https://github.com/algorandfoundation/algokit-utils-py/issues/134))
- Second batch of minor improvements based on internal feedback ([#133](https://github.com/algorandfoundation/algokit-utils-py/issues/133))
- Addressing feedback and minor tweaks ([#132](https://github.com/algorandfoundation/algokit-utils-py/issues/132))

# 2.4.0 - November 25th, 2024

## Features

- Puya debugging support ([#106](https://github.com/algorandfoundation/algokit-utils-py/issues/106))

## Fixes

- Removed incorrect decoding of rekey_to address. ([#121](https://github.com/algorandfoundation/algokit-utils-py/issues/121))
- Remove index on application create call in beta composer #122

# 2.3.2 - October 21st, 2024

## Fixes

- Adding state_change flag to simulate params (enables on chain section in extension) ([#109](https://github.com/algorandfoundation/algokit-utils-py/issues/109))
- Stop comment stripping from breaking base64

# 2.3.1 - August 8th, 2024

## Fixes

- Bumping mypy; making traces object typed to prevent misc mypy error on LogicError ([#105](https://github.com/algorandfoundation/algokit-utils-py/issues/105))
- Fixed obsolete info and broken links ([#100](https://github.com/algorandfoundation/algokit-utils-py/issues/100))

# 2.3.0 - May 13th, 2024

## Features

- AlgorandClient ([#71](https://github.com/algorandfoundation/algokit-utils-py/issues/71))

## Fixes

- Revert avoiding oncomplete ignore in app client calls (to be added as breaking change) ([#88](https://github.com/algorandfoundation/algokit-utils-py/issues/88))
- Add tests for transfer with rekey
- Audit
- Rekey transfer

# 2.2.2 - April 23rd, 2024

## Fixes

- Avoid ignoring `on_complete` if provided explicitly via transaction parameters ([#79](https://github.com/algorandfoundation/algokit-utils-py/issues/79))

# 2.2.1 - February 6th, 2024

## Fixes

- Handle updated LogicError format in algod 3.22 ([#68](https://github.com/algorandfoundation/algokit-utils-py/issues/68))
- Disable verbose logging level in config.py; only visible on debug log level now ([#62](https://github.com/algorandfoundation/algokit-utils-py/issues/62))

# 2.2.0 - December 15th, 2023

## Features

- Debugger related helpers and utils ([#61](https://github.com/algorandfoundation/algokit-utils-py/issues/61))

# 2.1.2 - November 22nd, 2023

# 2.1.1 - October 31st, 2023

## Fixes

- Handle TMPL_ variables with an underscore

# 2.1.0 - October 20th, 2023

## Features

- Task opt in and opt out ([#55](https://github.com/algorandfoundation/algokit-utils-py/issues/55))

# 2.0.1 - October 10th, 2023

## Fixes

- Adding missing TransactionParametersDict export ([#54](https://github.com/algorandfoundation/algokit-utils-py/issues/54))

# 2.0.0 - October 5th, 2023

## Breaking Changes

- Adding new client class for interacting with TestNet Dispenser API; Changing output type of ensure_funded method

## Features

- Adding support for interacting with dispenser api on testnet via ensure_funded; api client class ([#51](https://github.com/algorandfoundation/algokit-utils-py/issues/51))

# 1.4.0 - September 27th, 2023

## Features

- Transfer asset from one account to another ([#49](https://github.com/algorandfoundation/algokit-utils-py/issues/49))

## Fixes

- Adding simulate transaction with traces of debug mode ([#48](https://github.com/algorandfoundation/algokit-utils-py/issues/48))

# 1.3.1 - July 25th, 2023

## Fixes

- Add missing transaction parameters to CreateTransactionParameters ([#46](https://github.com/algorandfoundation/algokit-utils-py/issues/46))

# 1.3.0 - June 20th, 2023

## Features

- Deployment support for testnet and mainnet ([#45](https://github.com/algorandfoundation/algokit-utils-py/issues/45))

# 1.2.0 - June 6th, 2023

## Features

- Add factory method to Account to create from a new account
- Use official Algorand Docker images for LocalNet
- Add import_source_map and export_source_map to ApplicationClient
- Allow specifying app_name when creating an ApplicationClient ([#36](https://github.com/algorandfoundation/algokit-utils-py/issues/36))
- Use simulate for readonly methods
- Support partially providing template_values on client init
- Add signer and public_key to Account ([#35](https://github.com/algorandfoundation/algokit-utils-py/issues/35))

## Fixes

- Add a compatibility shim for simulate 3.15 endpoints
- Automatically provide an approval source_map where possible
- Also strip whitespace when stripping comments
- Add missing fields to CommonCallParametersDict

# 1.1.1 - May 3rd, 2023

## Fixes

- Return correct response when multiple transactions are in an ABI call ([#30](https://github.com/algorandfoundation/algokit-utils-py/issues/30))

# 1.1.0 - May 2nd, 2023

## Features

- Make ensure_funded funding_source parameter optional
- Add ensure_funded method ([#24](https://github.com/algorandfoundation/algokit-utils-py/issues/24))

## Fixes

- Handle quoted template variables
- Update strip_comments to handle quotes
- Remove deprecated/renamed functions
- Correctly adjust port in client configs ([#27](https://github.com/algorandfoundation/algokit-utils-py/issues/27))
- Fix network client auth headers ([#26](https://github.com/algorandfoundation/algokit-utils-py/issues/26))

# 1.0.3 - April 18th, 2023

## Fixes

- Strip comments before compiling to accomodate annotated teal ([#19](https://github.com/algorandfoundation/algokit-utils-py/issues/19))
- Stop transaction parameters being converted to dict ([#18](https://github.com/algorandfoundation/algokit-utils-py/issues/18))

# 1.0.2 - April 4th, 2023

## Fixes

- Handle non algosdk TransactionSigner implementations ([#14](https://github.com/algorandfoundation/algokit-utils-py/issues/14))
- Readd AppSpecStateDict type definition to root namespace

# 1.0.1 - March 29th, 2023

## Fixes

- Deprecate is_sandbox and get_sandbox_default_account ([#10](https://github.com/algorandfoundation/algokit-utils-py/issues/10))
- Rename sandbox to localnet

# 1.0.0 - March 28th, 2023

## Breaking Changes

- 1.0 release

# 0.2.0 - March 28th, 2023

## Features

- Allow broader types when specifying methods and app_spec in ApplicationClient ([#7](https://github.com/algorandfoundation/algokit-utils-py/issues/7))
- Make ABI call arguments kwargs instead of a dict ([#6](https://github.com/algorandfoundation/algokit-utils-py/issues/6))

# 0.1.3 - March 23rd, 2023

## Fixes

- Get_account now works if called a second time for the same account name

# 0.1.2 - March 23rd, 2023

## Fixes

- Expose execute_atc_with_logic_error, allow specifying approval source map
- Resolve sender on __init__
- Add rekey_to to call method ([#3](https://github.com/algorandfoundation/algokit-utils-py/issues/3))
- Handle app notes with partial data ([#2](https://github.com/algorandfoundation/algokit-utils-py/issues/2))

# 0.1.1 - March 22nd, 2023

## Fixes

- Don't mutate provided args when calling

# 0.1.0 - March 22nd, 2023

## Features

- Allow bytes for template_values
- Make DeleteApp when deploying one transaction across create and delete
- Add more details to deploy_app response
- Return ApplicationClient when deploying app
- Enum for on_update and on_schema_break behaviour
- Add template variables support
- Add idempotent deploy

## Fixes

- Add more typings
- Always find a clear state bare method
- Pass through additional call parameters
- Allow notes with type str
- Allow any type for arguments
- Fix incorrectly passing schema on bare calls
- ApplicationClient respects None values for allow_update or allow_delete if no deploy-time control being used
- Define more imports
- Define top level imports
- Typing fixes
- Review feedback
- Move wait for indexer function to tests
- Parse url and replace kmd port more robustly
- Reduce pyteal dependency, remove global ignores
- Apply changes from review
- Rename DeleteApp to ReplaceApp
- Fix ApplicationClient.prepare
- Make app_id and app_address on ApplicationClient readonly
- Re-add ALGOD_PORT and INDEXER_PORT support
- Ignore apps with no note prefix
