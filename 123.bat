::修改路径
set b=%~d0
set FilePath=%~dp0

::先当前的盘符
%b%
::先当前的路径
::set testcode = %FilePath%\testcode
::set testreport = %FilePath%\testreport

::不需要的时候注解掉
echo %FilePath%\testcode
cd %FilePath%\testcode
python test.py
python testinit.py

cd %FilePath%\testreport
python WriteHtmlApi.py