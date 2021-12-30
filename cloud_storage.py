import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A_Lzdk5hkT6WRLon5hrpj_uG_GKSroagJnOdYNlU4_lz3XMw0WZXrD8MaGrHQZVZVjcEoqzLH3qAdOgNZsVV2BTEJa0NCKgBRIQ5j6Mu66lORAV9tYzLMK7eMpjVD4iffdug_r0'
    transferData = TransferData(access_token)

    file_from = input("C:/Users/suman/Downloads/Pro98")
    file_to = input("C:/Users/suman/Downloads/Dropbox")
       
       # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()


    