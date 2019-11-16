# pack2md

Readme generator for StackStorm packs.  This tool will read the pack meta data, config schema,
action metadata and sensor metadata.  It will pass this information to a jinja2 template to
populate and produce a README file in markdown format.

## Installation

1. Create a virtualenv.
1. Install required modules.
1. Edit `README.jinja` to fit the packs needs (it should be located in the pack's root directory).
1. Run `pack2dm.py <pack_path>`.

## Example

An example of the pack documentation can be seen in the [livestatus](https://github.com/nzlosh/stackstorm_livestatus) pack.
