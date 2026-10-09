import json, random
T43 = """Shortcut to make selected text bold in Word|Ctrl+B|Ctrl+I|Ctrl+U|Ctrl+E|Ctrl+B applies bold. Ctrl+I is italic, Ctrl+U underline.
Shortcut to centre-align a paragraph in Word|Ctrl+E|Ctrl+L|Ctrl+R|Ctrl+J|Ctrl+E centres; L left, R right, J justify.
Shortcut to open the Find box in Word|Ctrl+F|Ctrl+H|Ctrl+G|Ctrl+K|Ctrl+H opens Replace, Ctrl+F opens Find (navigation pane).
Shortcut to select all content|Ctrl+A|Ctrl+S|Ctrl+Z|Ctrl+P|A stands for All.
Shortcut to undo the last action|Ctrl+Z|Ctrl+Y|Ctrl+X|Ctrl+V|Ctrl+Y redoes.
Shortcut to print a document|Ctrl+P|Ctrl+O|Ctrl+N|Ctrl+S|P stands for Print.
Shortcut to create a new document|Ctrl+N|Ctrl+O|Ctrl+W|Ctrl+Q|N stands for New.
Shortcut to open an existing file|Ctrl+O|Ctrl+N|Ctrl+P|Ctrl+E|O stands for Open.
Default file extension of Word 2007 and later|.docx|.doc|.dotx|.rtf|.doc was used by Word 97-2003; .docx is the XML-based format.
Extension of a Word template|.dotx|.docx|.xlsx|.pptx|.dotx (or .dot in older versions) is a template.
The Word feature that sends the same letter to many recipients|Mail Merge|Track Changes|Macro|Thesaurus|Mail Merge combines a main document with a data source.
Text that appears at the top of every page is a|Header|Footer|Footnote|Caption|Footers are at the bottom.
Text that appears at the bottom of every page is a|Footer|Header|Margin|Endnote|Page numbers are commonly placed here.
A note placed at the bottom of the same page to explain text is a|Footnote|Endnote|Comment|Header|Endnotes come at the end of the document.
Page orientation options in Word are|Portrait and Landscape|Horizontal and Diagonal|Tall and Short|Left and Right|Portrait is vertical; landscape is horizontal.
Feature that shows edits made by different reviewers|Track Changes|Mail Merge|Format Painter|Print Preview|Track Changes records insertions and deletions.
Tool used to copy formatting from one text to another|Format Painter|Find and Replace|Spell Check|Thesaurus|Format Painter is on the Home tab.
Pressing the Tab key in a table's last cell|Adds a new row|Deletes the table|Closes the table|Splits the table|A new row is added at the bottom.
Which key combination inserts a page break in Word?|Ctrl+Enter|Shift+Enter|Alt+Enter|Ctrl+Tab|Ctrl+Enter starts a new page.
The Word feature that suggests synonyms|Thesaurus|Spelling|Macro|Compare|Shift+F7 opens the Thesaurus.
Shortcut key for the spelling and grammar check in Word|F7|F5|F9|F12|F7 starts Spelling and Grammar.
A Save As dialog box in Word is opened by|F12|F1|F2|F10|F12 opens Save As.
In Excel, a formula must begin with|=|#|$|@|Every formula starts with an equals sign.
The intersection of a row and a column in Excel is a|Cell|Range|Sheet|Table|A cell such as B3.
The address of the cell in column C and row 5 is|C5|5C|C-5|R5C|Excel uses column letter then row number.
A group of selected cells is called a|Range|Row|Workbook|Chart|For example A1:B5.
The function that adds numbers in a range|SUM|ADD|TOTAL|PLUS|=SUM(A1:A5) adds the values.
The function that gives the mean of numbers|AVERAGE|MEAN|MEDIAN|MODE|=AVERAGE(A1:A5).
The function that returns the largest value|MAX|BIG|TOP|HIGH|=MAX(range).
The function that returns the smallest value|MIN|LOW|SMALL|BOTTOM|=MIN(range).
The function that counts cells containing numbers|COUNT|COUNTA|SUMIF|LEN|COUNTA counts non-empty cells of any kind.
The function used for a logical test with true/false results|IF|AND|SUM|TEXT|=IF(condition, value_if_true, value_if_false).
The function that looks up a value in the first column of a table|VLOOKUP|HLOOKUP|MATCH|INDEX|VLOOKUP searches vertically.
The symbol used to make a cell reference absolute|$|#|&|%|$A$1 stays fixed when copied.
The cell reference A1 copied one cell down becomes|A2|B1|A1|A0|Relative references shift with position.
The default name of the first worksheet in a new Excel workbook (recent versions)|Sheet1|Book1|Page1|Table1|Book1 is the workbook; Sheet1 is the worksheet.
Default file extension of an Excel workbook|.xlsx|.xls|.docx|.csv|.xls is the older format.
Shortcut to edit the active cell in Excel|F2|F4|F5|F7|F2 enters edit mode.
Pressing F4 while editing a reference|Cycles absolute and relative reference|Saves the file|Opens Help|Inserts a chart|F4 toggles $ signs.
The Excel feature that arranges data in ascending or descending order|Sort|Filter|Merge|Wrap|Sort is on the Data tab.
The Excel feature that shows only rows meeting a condition|Filter|Sort|Freeze|Group|AutoFilter hides non-matching rows.
The Excel feature that keeps header rows visible while scrolling|Freeze Panes|Split|Merge|Group|View tab, Freeze Panes.
An Excel graph with circular slices of a whole is a|Pie chart|Line chart|Bar chart|Scatter chart|Pie charts show proportions.
Joining several cells into one cell is called|Merge|Split|Wrap|Filter|Merge and Centre is on the Home tab.
The number of rows in recent versions of an Excel worksheet is about|1,048,576|65,536|16,384|256|Older .xls had 65,536 rows.
The number of columns in a recent Excel worksheet is|16,384|256|1,024|65,536|Columns go up to XFD.
The last column name in recent Excel is|XFD|ZZ|IV|XYZ|16,384 columns.
Shortcut to move to cell A1 in Excel|Ctrl+Home|Ctrl+End|Ctrl+A|Alt+Home|Ctrl+End goes to the last used cell.
The Excel error shown when dividing by zero|#DIV/0!|#NAME?|#VALUE!|#REF!|Dividing by zero is not allowed.
The Excel error shown for an unrecognised function name|#NAME?|#N/A|#NUM!|#NULL!|Usually a typo in the function name.
Shortcut key for the Save command|Ctrl+S|Ctrl+D|Ctrl+W|Ctrl+B|S stands for Save.
Ctrl+C and Ctrl+V are shortcuts for|Copy and Paste|Cut and Paste|Close and View|Create and Verify|Ctrl+X is Cut."""
T44 = """The brain of the computer is the|CPU|RAM|Monitor|Mouse|The Central Processing Unit executes instructions.
Full form of CPU|Central Processing Unit|Central Program Unit|Control Processing Unit|Core Peripheral Unit|It has an ALU and a control unit.
The part of the CPU that performs arithmetic and logic is the|ALU|CU|Cache|Register|ALU: Arithmetic Logic Unit.
Volatile memory that loses data when power is off|RAM|ROM|Hard disk|SSD|RAM is temporary working memory.
Memory that keeps start-up instructions permanently|ROM|RAM|Cache|Register|ROM is non-volatile.
Which is the smallest unit of data?|Bit|Byte|Nibble|Word|A bit is a 0 or 1.
How many bits make a byte?|8|4|16|2|One byte is 8 bits.
How many bytes are in a kilobyte (binary convention)?|1024|1000|512|2048|1 KB = 1024 bytes in the traditional convention.
Which is larger?|Gigabyte|Megabyte|Kilobyte|Byte|KB, MB, GB, TB in increasing order.
The binary number system has base|2|8|10|16|It uses only 0 and 1.
The decimal number 10 in binary is|1010|1001|1100|1110|8 + 2 = 10.
The hexadecimal system has base|16|8|10|2|It uses 0-9 and A-F.
A keyboard is an|Input device|Output device|Storage device|Processing device|It sends data to the computer.
A printer is an|Output device|Input device|Storage device|Memory|It produces hard copies.
A scanner is an|Input device|Output device|Software|Port|It converts documents to digital images.
A touchscreen is|Both input and output|Input only|Output only|Storage|It shows images and accepts touch.
Which of these is a storage device?|Hard disk|Scanner|Speaker|Keyboard|Also USB drives and SSDs.
SSD stands for|Solid State Drive|Super Speed Disk|Secure Storage Device|Static System Drive|SSDs have no moving parts.
Which device connects a computer to a network and converts signals?|Modem|Scanner|Plotter|Joystick|Modem: modulator-demodulator.
A device that connects several computers in a LAN|Switch|Printer|Scanner|Webcam|Switches forward data to the right device.
LAN stands for|Local Area Network|Large Area Network|Linked Access Node|Long Area Network|It covers a small area such as an office.
WAN stands for|Wide Area Network|Wireless Area Network|Web Access Network|World Area Node|The internet is the largest WAN.
The protocol used to load web pages|HTTP|SMTP|FTP|POP3|HTTPS is the secure version.
The protocol commonly used to send email|SMTP|HTTP|FTP|SNMP|SMTP: Simple Mail Transfer Protocol.
FTP is used for|Transferring files|Sending email|Browsing pages|Printing|File Transfer Protocol.
A URL is|A web address|A virus|A file type|A browser|Uniform Resource Locator.
An IP address identifies|A device on a network|A web page|A user's age|A file|It is a numeric label for a device.
DNS translates|Domain names to IP addresses|Files to folders|Emails to texts|Images to videos|Domain Name System.
Software that lets you browse websites|Web browser|Search engine|Compiler|Antivirus|Chrome, Edge, Firefox are examples.
A search engine is|A website that finds information|A browser|A virus|A protocol|Google and Bing are examples.
Which of these is an operating system?|Linux|Python|Oracle|Photoshop|Linux, Windows, macOS, Android.
Which is an example of system software?|Windows|MS Excel|Photoshop|Tally|It manages hardware and runs other software.
Which is application software?|MS Word|Linux|BIOS|Device driver|Application software does user tasks.
A programme that translates source code at once into machine code|Compiler|Interpreter|Assembler|Loader|An interpreter works line by line.
The lowest-level programming language|Machine language|Python|C++|Java|It consists of 0s and 1s.
DBMS stands for|Database Management System|Data Base Machine System|Digital Binary Memory System|Direct Backup Management System|MS Access and MySQL are examples.
In a database, a row is called a|Record|Field|Table|Query|A column is a field.
In a database, a column is called a|Field|Record|Report|Form|It holds one type of data.
A field that uniquely identifies each record|Primary key|Foreign key|Index|Query|No two records share a primary key value.
Malicious software designed to harm a computer|Malware|Firmware|Freeware|Shareware|Includes viruses, worms and ransomware.
Malware that locks files and demands payment|Ransomware|Spyware|Adware|Firmware|Do not pay; restore from backup.
Fake emails that trick users into sharing passwords|Phishing|Spooling|Booting|Cloning|Check the sender and links.
A security system that filters network traffic|Firewall|Router|Modem|Browser|It blocks unauthorised access.
Software that detects and removes viruses|Antivirus|Compiler|Driver|Spreadsheet|Keep it updated.
A strong password should|Mix letters, numbers and symbols|Be your name|Be 1234|Be your birth date|Longer and unique is better.
Making copies of important data is called|Backup|Formatting|Booting|Spooling|Keep backups in another place too.
Starting a computer is called|Booting|Formatting|Rebooting|Shutdown|Booting loads the OS.
Key combination to open Task Manager in Windows|Ctrl+Shift+Esc|Ctrl+Alt+Tab|Alt+F4|Win+L|Ctrl+Alt+Del also gives access.
Shortcut to switch between open windows|Alt+Tab|Ctrl+Tab|Alt+F4|Win+D|Alt+Tab cycles windows.
Shortcut to close the active window|Alt+F4|Ctrl+F4|Alt+Tab|Ctrl+Esc|Alt+F4 closes the program.
Shortcut to lock a Windows computer|Win+L|Win+D|Win+E|Win+R|Win+D shows the desktop."""
def build(raw, id_, slug, title, desc, seed):
    rnd = random.Random(seed); qs=[]
    for line in raw.strip().split('\n'):
        p=line.split('|'); assert len(p)==6, line
        q,c,w1,w2,w3,e=p; o=[c,w1,w2,w3]; assert len(set(x.lower() for x in o))==4,line
        rnd.shuffle(o); qs.append({'q':q,'o':o,'a':o.index(c),'e':e})
    print(slug,len(qs)); qs=qs[:50]; assert len(qs)==50
    json.dump({'id':id_,'slug':slug,'title':title,'desc':desc,'group':'Computer & IT','color':'#9333ea','questions':qs},open(f'src/data/tests/{id_:02d}-{slug}.json','w'),indent=1,ensure_ascii=False)
build(T43,43,'word-excel-deep-dive','Computer Skills III: MS Word & Excel Deep Dive','Shortcuts, formulas, functions and features asked in clerk tests',43)
build(T44,44,'hardware-networks-security','Computer Skills IV: Hardware, Networks, Databases & Security','CPU, memory, number systems, internet, databases and cyber safety',44)
