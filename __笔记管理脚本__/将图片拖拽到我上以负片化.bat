:: д������ָ���Ȼִ��batʱ������е�ÿ��ָ����ڹ�����
@echo off
:: %*���������ק��bat�ű��ϵ������ļ��ļ��ϣ���ð����ֵ�����ڱ������Ȼ������ú�����ʱ����ʹ��%*����ֵ�Ͳ�һ���ˣ�
set dragged_items=%*
:: %0������Ǹ��ļ��������ڵĵ�ַ����C:\Users\CSD\Documents\Enote_database\__batch_processor__\��ͼƬɶɶɶ.bat
set LocalPath=%0
:: �����ڵ��������Ǹ�execute_python_script������������Ϊ�ղ����õ�LocalPath
call :execute_python_script %LocalPath%
:: ��ʾһ�С��������ⰴť�Լ���...��
:: pause
exit

:execute_python_script
:: ����ĵȺź��дͬ��Ŀ¼���Ǹ�python�ű�������
set python_script=invertPICS.py
:: ���ǰѸղ�������ű������ �ļ���ַ �е��������ƣ���ͼƬɶɶɶ.bat����ɾ���ˣ�ʣ��һ��·����Ȼ���python�ű���·��������·��ƴ���������ͱ��python�ű���·����
:: ����Ȼǰ��϶�������ð�python�ű���bat�ű�����һ��Ŀ¼����=_=��
set file_path=%~dp1%python_script%
:: ������ڿ���ִ��python�ű��ˣ��������Ǹղ���ק��bat�ϵ���Щ�ļ�
python %file_path% %dragged_items%