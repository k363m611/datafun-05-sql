PS C:\Users\katherine.mcgaughey> DROP TABLE IF EXISTS books;
DROP : The term 'DROP' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, 
or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ DROP TABLE IF EXISTS books;
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (DROP:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\katherine.mcgaughey> DROP TABLE IF EXISTS authors;
DROP : The term 'DROP' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, 
or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ DROP TABLE IF EXISTS authors;
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (DROP:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\katherine.mcgaughey> 
PS C:\Users\katherine.mcgaughey> CREATE TABLE authors (
>>     author_id TEXT PRIMARY KEY,
>>     first_name TEXT,
>>     last_name TEXT,
>>     year_born INTEGER
>> );
author_id : The term 'author_id' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of 
the name, or if a path was included, verify that the path is correct and try again.
At line:2 char:5
+     author_id TEXT PRIMARY KEY,
+     ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (author_id:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\katherine.mcgaughey> 
PS C:\Users\katherine.mcgaughey> CREATE TABLE books (
>>     book_id TEXT PRIMARY KEY,
>>     title TEXT,
>>     year_published INTEGER,
>>     author_id TEXT,
>>     FOREIGN KEY (author_id) REFERENCES authors(author_id)
>> );
author_id : The term 'author_id' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of 
the name, or if a path was included, verify that the path is correct and try again.
At line:6 char:18
+     FOREIGN KEY (author_id) REFERENCES authors(author_id)
+                  ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (author_id:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
