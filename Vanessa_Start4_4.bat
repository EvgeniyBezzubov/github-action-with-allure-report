chcp 65001

For /F "Delims=." %%I In ('WMIC.exe OS Get LocalDateTime ^| Find "."') Do Set DT=%%I
Set FileName=%DT:~6,2%-%DT:~4,2%-%DT:~0,4%-%DT:~8,2%-%DT:~10,2%


"C:\Program Files (x86)\1cv8\8.3.25.1336\bin\1cv8c" /N"Администратор" /TestManager /Execute "C:\VA_Test\vanessa-automation\vanessa-automation-single.epf" /IBConnectionString "File=""C:\Users\User\Documents\infobase"";" /C"StartFeaturePlayer;VAParams=C:\VA_Test\VAParams4.json;VANESSA_ПутьКФайлуДляВыгрузкиСтатусаВыполненияСценариев=C:\VA_Test\allure-source\BuildStatus_%FileName%_infobase.log"
cd /d "C:\VA_Test\"
call allure generate --clean C:\Users\User\PycharmProjects\pythonProject1\some
cd C:\Users\User\PycharmProjects\pythonProject1\
git add .\
git commit -m "Автоматический коммит"
git push