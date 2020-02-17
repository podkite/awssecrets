import boto3


def _get_shell_style_string(secrets_dict):
    out = []
    for k in secrets_dict:
        out.append("%s=%s" % (k, secrets_dict[k]))
    return "\n".join(out)


def get_secrets(secrets, region_name):
    secrets_dict = {}
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    for s in secrets:
        get_secret_value_response = client.get_secret_value(
            SecretId=s
        )
        secrets_dict.update(eval(get_secret_value_response['SecretString']))
    return _get_shell_style_string(secrets_dict)
