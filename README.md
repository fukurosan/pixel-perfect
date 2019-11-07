# Pixel Perfect

Pixel Perfect is a fun, small little utility for encrypting images by shuffling the pixels around "seemingly" at random. Please note that this is just for fun, and not secure even in the slightest. I think it shows off a cool concept though.

## Running
```bash
python3 main.py --file myfile.png --operation encrypt
python3 main.py --file myfile_encrypted.png --operation decrypt
```

You have to use a lossless format in order for this to work. So basically no jpegs.

![Screenshot 1](/decrypted.png?raw=true)
![Screenshot 2](/encrypted.png?raw=true)