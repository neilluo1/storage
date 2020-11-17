import argparse

cases_parser = argparse.ArgumentParser(add_help=False)
cases_parser.add_argument("--cases", required=True, action="store", dest="cases", default=[], nargs='+', help="cases, default:None")

path_parser = argparse.ArgumentParser(add_help=False)
path_parser.add_argument("--path", action="store", dest="path", default=None, help="path, default: None")


def parse_arg():
    """Init all the command line arguments."""
    parser = argparse.ArgumentParser(description='pztest')
    subparsers = parser.add_subparsers()

    sub_parser = subparsers.add_parser('fs_mark', parents=[cases_parser, path_parser], help='ut args.')
    sub_parser.set_defaults(action='fs_mark')

    args = parser.parse_args()

    return args
