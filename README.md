# Secret Sauce Analytics

Lamba functions to process data from Amazon S3 buckets

### Package up the function code

```bash
7z a functions.zip lambda_function.py
```

### Create the Lambda function

```bash
 aws lambda create-function 
       --function-name secret-sauce-analytics 
       --runtime python3.7 
       --role arn:aws:iam::775297465882:role/service-role/secret-sauce 
       --handler lambda_function.handler 
       --zip-file fileb://functions.zip
``` 


### Update the function code

```bash
aws lambda update-function-code 
    --function-name secret-sauce-analytics 
    --zip-file fileb://functions.zip
```