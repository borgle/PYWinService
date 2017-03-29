@echo off

:: 安装windows服务
echo 正在安装服务，请稍候...
ServiceLauncher.exe -install -auto

:: 启动服务
sc start AmazonRankerService

echo 服务启动成功, 按任意键继续...
pause