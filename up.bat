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


@REM aws s3api put-object --body %cd%/%SOURCE% --bucket %BUCKET% --key %KEY% --profile %AWS_PROFILE% 
aws s3 cp %cd%/%SOURCE% s3://%BUCKET%/ --profile %AWS_PROFILE% && aws s3 ls s3://%BUCKET%/ --profile %AWS_PROFILE%