@echo off
set ENV="demo"
set AWS_ACCOUNT="edn"
set AWS_PROFILE="default"
set PRODUCT="ResumenTC"
set OWNER="ExperimentacionNegocio"
set COST_CENTER="99999"
set STACK=%AWS_ACCOUNT%-%ENV%-api-consulta
rem set BUCKET=%AWS_ACCOUNT%-s3-%ENV%-resumenes-deploys
set BUCKET="spvresumen"
set SOURCE=%1
set KEY=%2
set LAMBDA_FUNCTION=spvPoCResumen



aws lambda put-function-concurrency --function-name %LAMBDA_FUNCTION%  --reserved-concurrent-executions 0 --profile %AWS_PROFILE%