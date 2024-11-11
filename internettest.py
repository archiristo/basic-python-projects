import speedtest

test = speedtest.Speedtest()
upload = test.upload()
download = test.download()
upload = upload/1000000
download = download/1000000
print("uploading speed: ",upload)
print("downloading speed: ",download)