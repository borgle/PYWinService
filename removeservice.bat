@echo off

:: 停止服务
echo 正在停止服务，请稍候...
sc stop AmazonRankerService

echo 正在卸载服务...
:: 删除windows服务
ServiceLauncher.exe -remove

echo 服务卸载完成，请按任意键继续剩余卸载...
pause