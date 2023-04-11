import boto3
from botocore.exceptions import NoCredentialsError

session = boto3.Session(profile_name='personal')
credentials = session.get_credentials()

polly_client = boto3.client('polly',
                            aws_access_key_id=credentials.access_key,
                            aws_secret_access_key=credentials.secret_key,
                            aws_session_token=credentials.token)


result = polly_client.synthesize_speech(
    Text='Hello World!',
    OutputFormat='mp3',
    VoiceId='Aditi'
)

audio_stream = result['AudioStream'].read()
with open('helloworld.mp3', 'wb') as file:
    file.write(audio_stream)
