"""Send a DR run result to SNS."""

import argparse

import boto3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic-arn", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--message", required=True)
    args = parser.parse_args()

    sns = boto3.client("sns")
    sns.publish(
        TopicArn=args.topic_arn,
        Subject=args.subject,
        Message=args.message,
    )
    print("sent")


if __name__ == "__main__":
    main()
