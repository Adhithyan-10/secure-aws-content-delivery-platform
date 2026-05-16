import json
import urllib.parse
import urllib.request
import base64

def lambda_handler(event, context)
    try
        # 🔹 Get code
        code = event['queryStringParameters']['code']

        # 🔹 CONFIG (IMPORTANT)
        client_id = 58slmfv0vktsnba3h7aqvrqdh8
        client_secret = 1a1j1o8o9ten4rnusk7f045j3rg6tt66nbrspm8u8gsfchtb8i69   # 🔥 VERY IMPORTANT
        redirect_uri = httplocalhost5500

        token_url = httpsap-south-1jzcxwphkc.auth.ap-south-1.amazoncognito.comoauth2token

        # 🔹 Encode client_idclient_secret
        credentials = f{client_id}{client_secret}
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        # 🔹 Body
        data = urllib.parse.urlencode({
            grant_type authorization_code,
            client_id client_id,
            code code,
            redirect_uri redirect_uri
        }).encode(utf-8)

        # 🔹 Request
        req = urllib.request.Request(token_url, data=data)
        req.add_header(Content-Type, applicationx-www-form-urlencoded)
        req.add_header(Authorization, fBasic {encoded_credentials})

        # 🔹 Call Cognito
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        return {
            statusCode 200,
            headers {
                Access-Control-Allow-Origin ,
                Access-Control-Allow-Headers ,
                Access-Control-Allow-Methods 
            },
            body json.dumps(result)
        }

    except Exception as e
        return {
            statusCode 400,
            headers {
                Access-Control-Allow-Origin 
            },
            body json.dumps({
                error str(e)
            })
        }
