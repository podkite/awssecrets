import sys
import argparse as argp
from awssecrets import core


def _get_argparser():
    parser = argp.ArgumentParser(
        description="get aws secrets stored in AWS Secrets Manager"
    )
    parser.add_argument(
        "--secrets",
        required=True,
        nargs="+",
        help="list of secrets",
        dest="secrets",
    )
    parser.add_argument(
        "-r",
        "--region",
        help="aws region",
        dest="region_name",
    )
    return parser


def main():
    parser = _get_argparser()
    args = parser.parse_args(sys.argv[1:])
    region_name = args.region_name or "us-east-1"
    print(core.get_secrets(args.secrets, region_name))


if __name__ == "__main__":
    main()
