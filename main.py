"""
ETL-Query script
"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    create,
    read,
    update,
    delete,
    run_query,
)


def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "create",
            "read",
            "update",
            "delete",
            "run_query",
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)
    if args.action == "update":

        parser.add_argument("record_id", type=int)
        parser.add_argument("Flavour")
        parser.add_argument("Calories", type=int)
        parser.add_argument("Total_Fat_g", type=float)
        parser.add_argument("Trans_Fat_g", type=float)
        parser.add_argument("Carbohydrates_g", type=int)
        parser.add_argument("Sugars_g", type=int)
        parser.add_argument("Protein_g", type=float)
        parser.add_argument("Size")

    if args.action == "create":

        parser.add_argument("Flavour")
        parser.add_argument("Calories", type=int)
        parser.add_argument("Total_Fat_g", type=float)
        parser.add_argument("Trans_Fat_g", type=float)
        parser.add_argument("Carbohydrates_g", type=int)
        parser.add_argument("Sugars_g", type=int)
        parser.add_argument("Protein_g", type=float)
        parser.add_argument("Size")

    if args.action == "run_query":
        parser.add_argument("query")

    if args.action == "delete":
        parser.add_argument("record_id", type=int)

    # parse again with ever
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "update_record":
        update(
            args.record_id,
            args.Flavour,
            args.Calories,
            args.Total_Fat_g,
            args.Trans_Fat_g,
            args.Carbohydrates_g,
            args.Sugars_g,
            args.Protein_g,
            args.Size,
        )
    elif args.action == "delete":
        delete(args.record_id)
    elif args.action == "create":
        create(
            args.Flavour,
            args.Calories,
            args.Total_Fat_g,
            args.Trans_Fat_g,
            args.Carbohydrates_g,
            args.Sugars_g,
            args.Protein_g,
            args.Size,
        )
    elif args.action == "run_query":
        run_query(args.query)
    elif args.action == "read":
        data = read()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
