
import argparse

from . import util

# Top level arg parser.
arg_parser = argparse.ArgumentParser(prog="binaryaudit", description="Tools for ELF audit.")

# Top level args.
arg_parser.add_argument("--is-elf", action="store", metavar="/path/to/elf/file",
                        help="Determine whether a file is an ELF artifact. Exit is zero if true.")

telemetry_args = arg_parser.add_argument_group('telemetry arguments')
telemetry_args.add_argument('-t', '--enable-telemetry', action='store', required=False,
                            default="n", help="Enable the data storing to telemetry (default: n)")
telemetry_args.add_argument('-b', '--build-id', action='store', required=False,
                            help="Reference to the particular build.")
telemetry_args.add_argument('-d', '--product-name', action='store', required=False,
                            help="Name of the product to be tracked, e.g. a distro or a project name.")
telemetry_args.add_argument('-e', '--derivative', action='store', required=False,
                            help="Derivative name")
telemetry_args.add_argument('-u', '--buildurl', action='store', required=False,
                            help="Build URL")
telemetry_args.add_argument('-l', '--logurl', action='store', required=False,
                            help="URL of log files")

telemetry_args.add_argument('-v', '--verbose', action='store_true',
                            help="Verbose output.")

# If a subcommand has been called, read the name from args.cmd
arg_parser_subs = arg_parser.add_subparsers(help="Subcommands", dest="cmd")

# binaryaudit abi ...
# arg_parser_abi = arg_parser_subs.add_parser("abi", help="ABI tools.")

# binaryaudit rpm ...
arg_parser_rpm = arg_parser_subs.add_parser("rpm", help="RPM tools")

arg_parser_rpm_subs = arg_parser_rpm.add_subparsers(help="Subcommands", dest="rpm_cmd")

arg_parser_rpm_list = arg_parser_rpm_subs.add_parser(
        "list",
        help="Read RPM packages in a directory and create a list grouped by SRPM.")
arg_parser_rpm_list.add_argument('--source-dir', action="store", help="RPM package directory")
arg_parser_rpm_list.add_argument('--out-filename', action="store", help="Output filename")


# binaryaudit db ..
arg_parser_db = arg_parser_subs.add_parser("db", help="Database CLI wrapper.")


# ##### functions #####


def validate_telemetry_args(args):
    if args.enable_telemetry:
        if not args.build_id or not args.product_name or not args.derivative:
            util.fatal("With --enable-telemetry the options --build-id, --product-name and --derivative become required")
