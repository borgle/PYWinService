@echo off

:: ��װwindows����
echo ���ڰ�װ�������Ժ�...
ServiceLauncher.exe -install -auto

:: ��������
sc start AmazonRankerService

echo ���������ɹ�, �����������...
pause