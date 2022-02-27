# TagalogTranslatorMicroservice
Microservice for classmates application to translate between english and tagalog

This microservice performs a simple 2 way translation between English and Tagalog.

It runs in a separate process from the main file you are executing that needs the translation service.

To translate from either English or Tagalog first start the translator.py in a separate process from your main program

Then in your main program simply open the "from_eng_to_tagalog_in.txt" or "from_tagalog_to_eng_in.txt" and write whatever word you want translated to that file

Wait for the out.txt file to have text in it and read it, once file is read write back to the _out.txt file with "" so that it is once again empty

The current implementation has a 1 second sleep timer before re checking a file for changes --> think about using async functions to wait for response in the out file
the sleep timer can also be changed as needed for your requirements.
