echo off

call C:\Users\tcham\Anaconda3\Scripts\activate.bat
REM Change this path to where your scripth are located
cd C:\Users\tcham\Downloads\GetSampleImages

python %cd%\get_sample_images.py %cd%
REM python %cd%\1_smtp_API_script_for_sending_emails.py %cd%



echo.
echo " I am done ..." 
date /t
echo.
echo  END TIME: %time%

REM @pause
@pause

