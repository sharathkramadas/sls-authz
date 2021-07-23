import re
import jwt

def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource
                }
            ]
        }
    }

def authorize_request(event, context):
	try:		
		principalId = 'user:test'					
		token = event.get('authorizationToken')
		if token:			
			claims = jwt.decode(token, "secret", algorithms=["HS256"])			
			if claims.get('user',{}) == 'John':				
				return generate_policy(principalId, 'Allow', event['methodArn'])
			else:				
				return generate_policy(principalId, 'Deny', event['methodArn'])
	except BaseException as e:
		print(e)			
	return generate_policy(principalId, 'Deny', event['methodArn'])

