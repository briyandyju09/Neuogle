from docarray import Document

#Basic Input and cmd

print ("Hi! I am Neuogle, Your Jina ai based assistant")
x = input('Enter Your Command:')

if 'hi' in x:
    print("Hello There!")
    x = input("Enter Here:")

elif 'help' in x:
    print ("Hi! Type start-mango or start-custom to start and stop to stop")
    x = input("Enter here:") 
elif 'hello' in x:
    print("Hello There!")
    x = input("Enter Here:")

elif 'start-mango' in x:
    #jina ai code goes here
    d = Document(uri='http://clipart-library.com/image_gallery2/Mango-PNG.png')
    d.load_uri_to_image_tensor()

    print(d.tensor, d.tensor.shape)
    x = input("Enter Here:")

elif 'start-custom' in x:
    #jina ai code goes here
    a=input("url?:")
    d = Document(uri= a)
    d.load_uri_to_image_tensor()

    print(d.tensor, d.tensor.shape)
    x = input("Enter Here:")

elif 'stop' in x:
    print("bye, See you soon")
    exit()
    quit()
    
else:
    print("I didnt understand.")
    x = input("Enter Here:")

