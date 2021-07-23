## Serverless JWT Authorization - Python

### Prerequisites
* Python 3.8
* Python PIP
* Node
* NPM
* Httpie
* AWS credentials configured using `aws` cli

### Instructions

* Step 1: Install serverless module

```bash
npm install -g serverless
```

* Step 2: Install serverless plugins

```bash
sls plugin install -n serverless-python-requirements
```

* Step 3: Deploy function

```bash
sls deploy
```

* Step 4: Fetch the API Gateway url and run the function

```bash
http GET <your-gateway-url>
```

You should see a `401 Unauthorized`

* Step 5: Generate a JWT token

```bash
pip install pyjwt
```

```bash
python3 -c 'import jwt; print(jwt.encode({"user":"John"},"secret",algorithm="HS256"))'
```

Copy the token

* Step 6: Send an authorized request

```bash
http GET <your-gateway-url> Authorization:<your-token>
```

