

├── .gitignore
├── LICENSE.md
├── README.md
├── compile.sh
└── scr
    ├── classes.py
    ├── exceptions
        ├── __init__.py
        ├── routines_custom.py
        ├── sub_begin
        │   ├── __init__.py
        │   └── begin_custom.py
        └── sub_end
        │   ├── __init__.py
        │   └── end_custom.py
    ├── grammafy.py
    └── pyle_manager.py


/.gitignore:
--------------------------------------------------------------------------------
  1 | # Byte-compiled / optimized / DLL files
  2 | __pycache__/
  3 | *.py[cod]
  4 | *$py.class
  5 | 
  6 | # C extensions
  7 | *.so
  8 | 
  9 | # Distribution / packaging
 10 | .Python
 11 | build/
 12 | develop-eggs/
 13 | dist/
 14 | downloads/
 15 | eggs/
 16 | .eggs/
 17 | lib/
 18 | lib64/
 19 | parts/
 20 | sdist/
 21 | var/
 22 | wheels/
 23 | share/python-wheels/
 24 | *.egg-info/
 25 | .installed.cfg
 26 | *.egg
 27 | MANIFEST
 28 | 
 29 | # PyInstaller
 30 | #  Usually these files are written by a python script from a template
 31 | #  before PyInstaller builds the exe, so as to inject date/other infos into it.
 32 | *.manifest
 33 | *.spec
 34 | 
 35 | # Installer logs
 36 | pip-log.txt
 37 | pip-delete-this-directory.txt
 38 | 
 39 | # Unit test / coverage reports
 40 | htmlcov/
 41 | .tox/
 42 | .nox/
 43 | .coverage
 44 | .coverage.*
 45 | .cache
 46 | nosetests.xml
 47 | coverage.xml
 48 | *.cover
 49 | *.py,cover
 50 | .hypothesis/
 51 | .pytest_cache/
 52 | cover/
 53 | 
 54 | # Translations
 55 | *.mo
 56 | *.pot
 57 | 
 58 | # Django stuff:
 59 | *.log
 60 | local_settings.py
 61 | db.sqlite3
 62 | db.sqlite3-journal
 63 | 
 64 | # Flask stuff:
 65 | instance/
 66 | .webassets-cache
 67 | 
 68 | # Scrapy stuff:
 69 | .scrapy
 70 | 
 71 | # Sphinx documentation
 72 | docs/_build/
 73 | 
 74 | # PyBuilder
 75 | .pybuilder/
 76 | target/
 77 | 
 78 | # Jupyter Notebook
 79 | .ipynb_checkpoints
 80 | 
 81 | # IPython
 82 | profile_default/
 83 | ipython_config.py
 84 | 
 85 | # pyenv
 86 | #   For a library or package, you might want to ignore these files since the code is
 87 | #   intended to run in multiple environments; otherwise, check them in:
 88 | # .python-version
 89 | 
 90 | # pipenv
 91 | #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
 92 | #   However, in case of collaboration, if having platform-specific dependencies or dependencies
 93 | #   having no cross-platform support, pipenv may install dependencies that don't work, or not
 94 | #   install all needed dependencies.
 95 | #Pipfile.lock
 96 | 
 97 | # poetry
 98 | #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
 99 | #   This is especially recommended for binary packages to ensure reproducibility, and is more
100 | #   commonly ignored for libraries.
101 | #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
102 | #poetry.lock
103 | 
104 | # pdm
105 | #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
106 | #pdm.lock
107 | #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
108 | #   in version control.
109 | #   https://pdm.fming.dev/#use-with-ide
110 | .pdm.toml
111 | 
112 | # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
113 | __pypackages__/
114 | 
115 | # Celery stuff
116 | celerybeat-schedule
117 | celerybeat.pid
118 | 
119 | # SageMath parsed files
120 | *.sage.py
121 | 
122 | # Environments
123 | .env
124 | .venv
125 | env/
126 | venv/
127 | ENV/
128 | env.bak/
129 | venv.bak/
130 | 
131 | # Spyder project settings
132 | .spyderproject
133 | .spyproject
134 | 
135 | # Rope project settings
136 | .ropeproject
137 | 
138 | # mkdocs documentation
139 | /site
140 | 
141 | # mypy
142 | .mypy_cache/
143 | .dmypy.json
144 | dmypy.json
145 | 
146 | # Pyre type checker
147 | .pyre/
148 | 
149 | # pytype static type analyzer
150 | .pytype/
151 | 
152 | # Cython debug symbols
153 | cython_debug/
154 | 
155 | # PyCharm
156 | #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
157 | #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
158 | #  and can be added to the global gitignore or merged into this file.  For a more nuclear
159 | #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
160 | #.idea/
161 | 


--------------------------------------------------------------------------------
/LICENSE.md:
--------------------------------------------------------------------------------
 1 | MIT License
 2 | 
 3 | Copyright (c) 2023 Tommaso Seneci
 4 | 
 5 | Permission is hereby granted, free of charge, to any person obtaining a copy
 6 | of this software and associated documentation files (the "Software"), to deal
 7 | in the Software without restriction, including without limitation the rights
 8 | to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 9 | copies of the Software, and to permit persons to whom the Software is
10 | furnished to do so, subject to the following conditions:
11 | 
12 | The above copyright notice and this permission notice shall be included in all
13 | copies or substantial portions of the Software.
14 | 
15 | THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16 | IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17 | FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18 | AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19 | LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20 | OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21 | SOFTWARE.
22 | 


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
 1 | # grammafy 1.4.5
 2 | 
 3 | This script serves the purpose of cleaning up tex files by creating a txt file, stripped of all the commands, that can be fed to typying software such as Grammarly. Formulas are substituted with the symbol `[_]`, and the other changes should be comprehensible.
 4 | 
 5 | I don't ask for money, but please give a star to the repository if you have found my program useful :)
 6 | 
 7 | ## installation and use
 8 | 
 9 | Needs Python >= 3.10. Download the latest release and run grammafy.py from terminal
10 | ```
11 | python3 grammafy.py
12 | ```
13 | Select the main tex file by navigating with the arrows and pressing enter on it (see [terminal file manager](https://github.com/ttoommxx/pylePicker) )
14 | 
15 | If you want the latest hotfixes, clone the main branch of this GitHub page.
16 | 
17 | ## debugging mode
18 | 
19 | This script follows a strict philosophy: every command knows exactly what is doing and nothing else, and can only see the tex file as a string (`source`), the cleaned-up file (`clean`) and the file path.
20 | 
21 | The script computes the following instructions:
22 | 1) Everything written before `\begin{document}` is immediately removed and the rest of the tex file is saved into a big string called `source.text`.
23 | 2) The program scans `source.text` looking for the following symbols:
24 | ```
25 | \ , { , } , $ , % , ~
26 | ```
27 | 3) If it finds any of the above, it prints everything to `clean.text` up until such symbol, by calling `clean.add(text)`, and executes an action depending on the symbol.
28 | 4) If the special character ``\`` is found, the script interprets the command as everything in between `\` and
29 | ```
30 | { , } , . , , , : , ; , [ , ] , ( , ) , $ , \ , \n , " , ' , ~
31 | ```
32 | At this point, I wrote most of the built in commands. If you want to add your own, please add to any of the custom py modules following the provided templates. Also the void files constitute a list of void commands.
33 | 5) If the command if found, the index of `source` is moved right at the end of it and the command is run.
34 | 6) I included two special routines, `begin` and `end` that have their own folder modules.
35 | 7) At the end of execution, the script writes `clean.text` in a file ending with `_grammafied.txt`, and saves the unknown commands in a file ending with `_unknowns.txt`.
36 | 
37 | # WARNING
38 | 
39 | The script can handle pretty much everything and will always reach completion, under the assumption that the file compiles properly (though the script doesn't compile). There might be instances where it gives the wrong output. This is mostly when the tex file is poorly written. For example, when using nested equations like
40 | ```
41 | $ (e^x)^{-1} \text{ $ = $ } e^{-x} $. 
42 | ```
43 | The script does handle properly nested unknown commands such as
44 | ```
45 | \begin{hello} This environemnt does nothing, \begin{hello} as you can see \end{hello} \end{hello}.
46 | ```
47 | When writing a (custom) subroutine, it is not necessary to include the symbol *. The script is written so that such a symbol is simply ignored.
48 | 
49 | ## disclaimers
50 | 
51 | This project is not intended to be a fully working application, at least at the moment. It was developed to facilitate correcting typos in my dissertation thesis, and because it works well enough I thought that sharing it with everyone would be a good idea. If you want to help me with this project or have any suggestions, do not hesitate to reach out to me by email.
52 | 
53 | # to do
54 | 
55 | - I am thiking of adding pre and post operations.
56 | 


--------------------------------------------------------------------------------
/compile.sh:
--------------------------------------------------------------------------------
 1 | #!/bin/bash
 2 | 
 3 | installed_packages=$(pip list)
 4 | 
 5 | if echo "$installed_packages" | grep "Uni-Curses"; then
 6 |     if echo "$installed_packages" | grep "pyinstaller"; then
 7 |         rm -rf build
 8 |         rm -rf dist
 9 |         pyinstaller --onefile scr/grammafy.py
10 |         exit 0
11 |     else
12 |         echo "Error: pyinstaller is not installed via pip, run pip install mypy"
13 |     fi
14 | else
15 |     echo "Error: unicurses is not installed via pip, run pip install uni-curses"
16 | fi
17 | exit 1
18 | 


--------------------------------------------------------------------------------
/scr/classes.py:
--------------------------------------------------------------------------------
  1 | """main objects used by grammafy main execution"""
  2 | 
  3 | 
  4 | class Node:
  5 |     """NodeList class contained source code to be cleaned, ordered from head"""
  6 | 
  7 |     def __init__(self, text, root=None) -> None:
  8 |         self._text = (
  9 |             "\n".join(
 10 |                 filter(lambda x: not x.lstrip().startswith("%"), text.splitlines())
 11 |             )
 12 |             + "\n"
 13 |         )
 14 |         self._index = 0
 15 |         self.root = root
 16 |         self.symbols = {"\\": -1, "{": -1, "}": -1, "

quot;: -1, "%": -1, "~": -1}
 17 | 
 18 |     @property
 19 |     def text(self) -> str:
 20 |         """return the text from the current index"""
 21 |         return self._text[self.index :]
 22 | 
 23 |     @text.setter
 24 |     def text(self, text: str) -> None:
 25 |         """does not allow for modifying the source code"""
 26 |         raise ValueError("text is a constant and should not be changed")
 27 | 
 28 |     @property
 29 |     def index(self) -> int:
 30 |         """return the current index"""
 31 |         return self._index
 32 | 
 33 |     @index.setter
 34 |     def index(self, index: int) -> None:
 35 |         """set the index and reset if analysing backwards, this way if functions are poorly programmer the script won't loop"""
 36 |         if index < self._index:
 37 |             print("index overload: the index has been reset")
 38 |             self._index = len(self._text)
 39 |         else:
 40 |             self._index = index
 41 | 
 42 |     @property
 43 |     def inter(self) -> int:
 44 |         """this functions search for the first symbol occurrence that has already been analysed yet, i.e. that precedes the current index"""
 45 |         for x in list(self.symbols.keys()):
 46 |             if self.symbols[x] < self.index:  # update only those that haven't been used
 47 |                 if x not in self.text:
 48 |                     self.symbols.pop(x)
 49 |                 else:
 50 |                     self.symbols[x] = self._text.find(x, self.index)
 51 |         if any(self.symbols):
 52 |             return min(self.symbols.values()) - self.index
 53 |         else:
 54 |             return -1
 55 | 
 56 |     def move_index(self, text_to_find: str) -> None:
 57 |         """search for text_to_find and move index at the end of the text"""
 58 |         self.index = self._text.find(text_to_find, self.index) + len(text_to_find)
 59 | 
 60 | 
 61 | class Source:
 62 |     """mock class that behaves like the head of the ListNode (inherits most of its attributes) and pops the head when it's been fully analysed"""
 63 | 
 64 |     def __init__(self, text: str) -> None:
 65 |         self.head = Node(text)
 66 | 
 67 |     # <<< treat this class as the actual head of the node
 68 |     @property
 69 |     def index(self) -> int:
 70 |         """return index of head"""
 71 | 
 72 |         return self.head.index
 73 | 
 74 |     @index.setter
 75 |     def index(self, val: int) -> None:
 76 |         self.head.index = val
 77 | 
 78 |     @property
 79 |     def text(self) -> str:
 80 |         """return text of head"""
 81 | 
 82 |         return self.head.text
 83 | 
 84 |     @text.setter
 85 |     def text(self, val: str) -> None:
 86 |         self.head.text = val
 87 | 
 88 |     @property
 89 |     def inter(self) -> int:
 90 |         """return inter of head"""
 91 | 
 92 |         return self.head.inter
 93 | 
 94 |     def move_index(self, text_to_find: str) -> None:
 95 |         """inherits the move_index function from Node"""
 96 |         self.head.move_index(text_to_find)
 97 | 
 98 |     # >>>
 99 | 
100 |     def add(self, text: str) -> None:
101 |         """add a new node and set it as head"""
102 |         self.head = Node(text, self.head)
103 | 
104 |     def pop(self) -> None:
105 |         """remove the current node, keeping the object as is"""
106 |         self.head = self.head.root
107 | 
108 | 
109 | class Clean:
110 |     """class that contains the cleaned up tex code"""
111 | 
112 |     def __init__(self):
113 |         self._text = []
114 |         # aggessive mode, we are going to store all the skipped command in one .txt file
115 |         self.aggro = set()
116 | 
117 |     def add(self, text: str) -> None:
118 |         """add new cleaned text"""
119 |         self._text.append(text)
120 | 
121 |     @property
122 |     def text(self) -> str:
123 |         """when being called, it assembles the code that has been added and returns it, keeping it in memory in case its called again"""
124 |         if len(self._text) > 1:
125 |             self._text = ["".join(self._text)]
126 |         return self._text[0]
127 | 
128 |     @text.setter
129 |     def text(self, text: str) -> None:
130 |         """when setting the text, it clears the queue"""
131 |         self._text = [text]
132 | 


--------------------------------------------------------------------------------
/scr/exceptions/__init__.py:
--------------------------------------------------------------------------------
  1 | """routine modules initialiser"""
  2 | 
  3 | # ----------------------------------------
  4 | # BUILT-IN FUNCTIONS
  5 | # ----------------------------------------
  6 | 
  7 | 
  8 | def _reprint(env) -> None:
  9 |     """add the command to env.clean the command"""
 10 |     env.clean.add(env.command)
 11 | 
 12 | 
 13 | def _curly(env) -> None:
 14 |     """move to the end of curly brackets"""
 15 |     env.source.move_index("}")
 16 | 
 17 | 
 18 | def _curly_curly(env) -> None:
 19 |     """move to the end for 2 consecutive curly brackets"""
 20 |     env.source.move_index("}")
 21 |     env.source.move_index("}")
 22 | 
 23 | 
 24 | def _color(env) -> None:
 25 |     """add color to env.source and move to the end of curly brackets"""
 26 |     env.clean.add("Color:")
 27 |     i = env.source.text.find("}")
 28 |     env.clean.add(env.source.text[1:i].upper())
 29 |     env.source.index += i + 1
 30 | 
 31 | 
 32 | def _footnote(env) -> None:
 33 |     """add footnote to env.source and move to the end of nested curly brackets"""
 34 |     i = 1
 35 |     j = i  # index for open brackets
 36 |     while i >= j and j > 0:
 37 |         i = env.source.text.find("}", i) + 1
 38 |         j = env.source.text.find("{", j) + 1
 39 | 
 40 |     # add the text in the footnote to the queue in parenthesis
 41 |     env.source.add("(FOOTNOTE: " + env.source.text[1 : i - 1] + ")")
 42 |     env.source.root.index += i
 43 | 
 44 | 
 45 | def _include(env) -> None:
 46 |     r"""responds to \include command and adds the new env.source to the head of env.source. The included files need to be in the same folder"""
 47 |     i = env.source.text.find("}")
 48 |     include_path = env.source.text[1:i]
 49 | 
 50 |     if include_path.endswith(".bbl"):  # skip bibliography files
 51 |         env.source.index += i + 1
 52 |     else:
 53 |         if not include_path.endswith(".tex"):  # if the extension is not present
 54 |             include_path += ".tex"
 55 |         with open(f"{env.folder_path}{include_path}", encoding="utf-8") as include_tex:
 56 |             env.source.add(include_tex.read())
 57 |         env.source.root.index += i + 1
 58 | 
 59 | 
 60 | def _print_curly(env) -> None:
 61 |     """[_] to env.clean when meeting curly brackets and move to the end of curly brackets"""
 62 |     env.clean.add("[_]")
 63 |     env.source.move_index("}")
 64 | 
 65 | 
 66 | def _print_square_curly(env) -> None:
 67 |     """add [_] for env.clean and move to the end of square if present, and then curly brackets"""
 68 |     env.clean.add("[_]")
 69 |     if env.source.text[0] == "[":
 70 |         env.source.move_index("]")
 71 |     env.source.move_index("}")
 72 | 
 73 | 
 74 | from exceptions import sub_begin
 75 | 
 76 | 
 77 | def _begin(env) -> None:
 78 |     """responds to the command being and move to the function begin and its subroutines"""
 79 |     i = env.source.text.find("}")  # right next after the brackets
 80 |     env.command = env.source.text[1:i]  # remove asterisk if any
 81 |     env.source.move_index("}")
 82 |     sub_begin.interpret(env)
 83 | 
 84 | 
 85 | from exceptions import sub_end
 86 | 
 87 | 
 88 | def _end(env) -> None:
 89 |     """responds to the command end and move to the function end and its subroutines"""
 90 |     i = env.source.text.find("}")
 91 |     env.command = env.source.text[1:i]
 92 |     env.source.move_index("}")
 93 |     sub_end.interpret(env)
 94 | 
 95 | 
 96 | # special commands (not include command to avoid string problems)
 97 | 
 98 | 
 99 | def _new_line(env) -> None:
100 |     """add a new line to env.clean"""
101 |     env.clean.add("\n")
102 |     env.source.index += 1
103 | 
104 | 
105 | def _square_equation(env) -> None:
106 |     r"""add [_] when meeting an equation called via \[ and move index to the end if it"""
107 |     i = env.source.text.find("\\]")
108 |     env.clean.add("[_]")
109 |     if env.source.text[:i].rstrip()[-1] in [
110 |         ",",
111 |         ";",
112 |         ".",
113 |     ]:  # add punctuation to non-inline equations
114 |         env.clean.add(env.source.text[:i].rstrip()[-1])
115 |     env.source.move_index("\\]")
116 | 
117 | 
118 | def _round_equation(env) -> None:
119 |     r"""add [_] when meeting an equation called via \( and move index to the end if it"""
120 |     i = env.source.text.find("\\)")
121 |     env.clean.add("[_]")
122 |     if env.source.text[:i].rstrip()[-1] in [
123 |         ",",
124 |         ";",
125 |         ".",
126 |     ]:  # add punctuation to non-inline equations
127 |         env.clean.add(env.source.text[:i].rstrip()[-1])
128 |     env.source.move_index("\\)")
129 | 
130 | 
131 | def _apostrofe(env) -> None:
132 |     """skip letter when meeting an apostrofe"""
133 |     if env.source.text[1] in ("a", "e", "i", "o", "u"):
134 |         env.source.index += 1
135 | 
136 | 
137 | def _tilde(env) -> None:
138 |     """add tilde to env.clean"""
139 |     env.clean.add("~")
140 |     env.source.index += 1
141 | 
142 | 
143 | def _null_function(env) -> None:
144 |     """null function, does nothing"""
145 | 
146 | 
147 | # ----------------------------------------
148 | # VARIABLES
149 | # ----------------------------------------
150 | 
151 | from .routines_custom import void_c
152 | 
153 | void = (
154 |     "centering",
155 |     "small",
156 |     "large",
157 |     "Large",
158 |     "newpage",
159 |     "textbf",
160 |     "textit",
161 |     "emph",
162 |     "maketitle",
163 |     "tableofcontents",
164 |     "footnotesize",
165 |     "selectfont",
166 |     "author",
167 |     "title",
168 |     "date",
169 |     "Huge",
170 |     "huge",
171 |     "underline",
172 |     "chapter",
173 |     "section",
174 |     "subsection",
175 |     "subsubsection",
176 |     "section*",
177 |     "subsection*",
178 |     "subsubsection*",
179 |     "text",
180 |     "bbox",
181 |     "clearpage",
182 |     "appendix",
183 |     "p",
184 |     "S",
185 |     "compat",
186 |     "bf",
187 |     "em",
188 |     "printbibliography",
189 |     "bigskip",
190 |     "mbox",
191 |     "preprint",
192 |     "affiliation",
193 |     "noindent",
194 |     "texorpdfstring",
195 |     "it",
196 |     "address",
197 |     "thanks",
198 |     "textsc",
199 |     "texttt",
200 | )
201 | 
202 | from .routines_custom import dic_commands_c
203 | 
204 | dic_commands = {
205 |     "addchap": _curly,
206 |     "addsec": _curly,
207 |     "begin": _begin,
208 |     "bibliography": _curly,
209 |     "bibliographystyle": _curly,
210 |     "chaptermark": _curly,
211 |     "cite": _print_square_curly,
212 |     "color": _color,
213 |     "cref": _print_curly,
214 |     "Cref": _print_curly,
215 |     "email": _curly,
216 |     "end": _end,
217 |     "eqref": _print_curly,
218 |     "fontfamily": _curly,
219 |     "footnote": _footnote,
220 |     "hspace": _curly,
221 |     "include": _include,
222 |     "includegraphics": _curly,
223 |     "input": _include,
224 |     "label": _curly,
225 |     "pagenumbering": _curly,
226 |     "pagestyle": _curly,
227 |     "ref": _print_curly,
228 |     "renewcommand": _curly_curly,
229 |     "setlength": _curly_curly,
230 |     "thispagestyle": _curly,
231 |     "vspace": _curly,
232 |     "&": _reprint,
233 |     "%": _reprint,
234 |     "#": _reprint,
235 | }
236 | 
237 | special_commands = {
238 |     "[": _square_equation,
239 |     "(": _round_equation,
240 |     '"': _apostrofe,
241 |     "'": _apostrofe,
242 |     "\\": _new_line,
243 |     "\n": _new_line,
244 |     "~": _tilde,
245 | }
246 | 
247 | # ----------------------------------------
248 | # INTERPRETER
249 | # ----------------------------------------
250 | 
251 | 
252 | def interpret(env) -> None:
253 |     """this is the custom interpreter that recalls first custom subroutines, then built-in subroutines and then skip the command if not recognised"""
254 |     if env.command:
255 |         if env.command in void or env.command in void_c:
256 |             pass
257 |         elif env.command in dic_commands_c:
258 |             dic_commands_c[env.command](env)
259 |         elif env.command in dic_commands:
260 |             dic_commands[env.command](env)
261 |         else:
262 |             while env.source.text[0] in [
263 |                 "{",
264 |                 "[",
265 |             ]:  # check if opening and closing brackets
266 |                 if env.source.text[0] == "{":
267 |                     i = env.source.text.find("{", 1)
268 |                     j = env.source.text.find("}", 1)
269 |                     while 0 < i < j:
270 |                         i = env.source.text.find("{", i + 1)
271 |                         j = env.source.text.find("}", j + 1)
272 |                     env.source.index += j + 1
273 |                 else:
274 |                     i = env.source.text.find("[", 1)
275 |                     j = env.source.text.find("]", 1)
276 |                     while 0 < i < j:
277 |                         i = env.source.text.find("[", i + 1)
278 |                         j = env.source.text.find("]", j + 1)
279 |                     env.source.index += j + 1
280 |             env.clean.aggro.add(env.command)
281 |     else:  # empty string
282 |         env.command = env.source.text[0]
283 |         if env.command in special_commands:
284 |             special_commands[env.command](env)
285 |         else:
286 |             env.clean.add(" ")
287 |             env.source.index += 1
288 | 
289 | 
290 | # ----------------------------------------
291 | 


--------------------------------------------------------------------------------
/scr/exceptions/routines_custom.py:
--------------------------------------------------------------------------------
 1 | """custom routines"""
 2 | 
 3 | # ----------------------------------------
 4 | # FUNCTIONS
 5 | # ----------------------------------------
 6 | 
 7 | 
 8 | def _print_curly(env) -> None:
 9 |     """add [_] to CLEAN when meeting curly brackets and move to the end of curly brackets"""
10 |     env.clean.add("[_]")
11 |     env.source.move_index("}")
12 | 
13 | 
14 | # ----------------------------------------
15 | # VARIABLES
16 | # ----------------------------------------
17 | 
18 | dic_commands_c = {
19 |     "citep": _print_curly,
20 |     "eqrefp": _print_curly,
21 |     "refp": _print_curly,
22 | }
23 | 
24 | void_c = (
25 |     "marker",
26 |     "bookmark",
27 | )
28 | 
29 | 
30 | # TEMPLATE
31 | # dic_commands_c = {
32 | #     "{name_command}" : "_{name_function}",
33 | # }
34 | 


--------------------------------------------------------------------------------
/scr/exceptions/sub_begin/__init__.py:
--------------------------------------------------------------------------------
  1 | """being routines initialiser"""
  2 | 
  3 | # ----------------------------------------
  4 | # BULTI-IN FUNCTIONS
  5 | # ----------------------------------------
  6 | 
  7 | 
  8 | def _title(env) -> None:
  9 |     """add title to env.clean"""
 10 |     env.clean.add(env.command.title() + ".")
 11 | 
 12 | 
 13 | def _equation(env) -> None:
 14 |     """add [_] and move to the end of the equation command"""
 15 |     env.clean.add("[_]")
 16 |     # find the index where the whole portion ends
 17 |     i = env.source.text.find("\\end{" + env.command + "}")  # from here, use regex
 18 |     if env.source.text[: i - 1].rstrip()[-1] in [",", ";", "."]:
 19 |         env.clean.add(env.source.text[: i - 1].rstrip()[-1])
 20 |     env.source.move_index("\\end{" + env.command + "}")
 21 | 
 22 | 
 23 | def _enumerate(env) -> None:
 24 |     """add a new node to env.source, replacing item with . followed by a new number"""
 25 |     if env.source.text[0] == "[":
 26 |         env.source.move_index("]")
 27 |     i = env.source.text.find("\\end{enumerate}")
 28 |     new_text = env.source.text[:i]
 29 |     index_enum = 1
 30 |     while "\\item" in new_text:
 31 |         new_text = new_text.replace("\\item", str(index_enum) + ".", 1)
 32 |         index_enum += 1
 33 | 
 34 |     env.source.add(new_text)
 35 |     env.source.root.move_index("\\end{enumerate}")
 36 | 
 37 | 
 38 | def _itemize(env) -> None:
 39 |     """add a new node to env.source, replacing item with -"""
 40 |     if env.source.text[0] == "[":
 41 |         env.source.move_index("]")
 42 |     i = env.source.text.find("\\end{itemize}")
 43 |     new_text = env.source.text[:i].replace("\\item", "-")
 44 | 
 45 |     env.source.add(new_text)
 46 |     env.source.root.move_index("\\end{itemize}")
 47 | 
 48 | 
 49 | def _curly_curly(env) -> None:
 50 |     """move index by two curly brackets"""
 51 |     env.source.move_index("}")
 52 |     env.source.move_index("}")
 53 | 
 54 | 
 55 | def _curly_curly_curly(env) -> None:
 56 |     """move index by 3 curly brackets"""
 57 |     for _ in range(3):
 58 |         env.source.move_index("}")
 59 | 
 60 | 
 61 | def _skip(env) -> None:
 62 |     """skip command when not recognised"""
 63 |     env.source.move_index("\\end{" + env.command + "}")
 64 | 
 65 | 
 66 | # ----------------------------------------
 67 | # VARIABLES
 68 | # ----------------------------------------
 69 | 
 70 | from .begin_custom import void_c
 71 | 
 72 | void = ("center", "frame")
 73 | 
 74 | from .begin_custom import dic_commands_c
 75 | 
 76 | dic_commands = {
 77 |     "abstract": _title,
 78 |     "align": _equation,
 79 |     "align*": _equation,
 80 |     "equation": _equation,
 81 |     "equation*": _equation,
 82 |     "comment": _title,
 83 |     "conjecture": _title,
 84 |     "corollary": _title,
 85 |     "definition": _title,
 86 |     "enumerate": _enumerate,
 87 |     "eqnarray": _equation,
 88 |     "eqnarray*": _equation,
 89 |     "figure": _equation,
 90 |     "figure*": _equation,
 91 |     "gather": _equation,
 92 |     "gather*": _equation,
 93 |     "lemma": _title,
 94 |     "minipage": _curly_curly,
 95 |     "multline": _equation,
 96 |     "multline*": _equation,
 97 |     "proof": _title,
 98 |     "proposition": _title,
 99 |     "question": _title,
100 |     "remark": _title,
101 |     "table": _equation,
102 |     "thebibliography": _skip,
103 |     "theorem": _title,
104 |     "tikzpicture": _equation,
105 |     "verbatim": _equation,
106 |     "wrapfigure": _curly_curly_curly,
107 |     "itemize": _itemize,
108 | }
109 | 
110 | # ----------------------------------------
111 | # INTERPRETER
112 | # ----------------------------------------
113 | 
114 | 
115 | def interpret(env) -> None:
116 |     """custom interpreted for the begin routine, works similarly to the main interpreter"""
117 |     if env.command in void or env.command in void_c:
118 |         pass
119 |     elif env.command in dic_commands_c:
120 |         dic_commands_c[env.command](env)
121 |     elif env.command in dic_commands:
122 |         dic_commands[env.command](env)
123 |     else:
124 |         i = env.source.text.find("\\begin{" + env.command + "}", 6)
125 |         j = env.source.text.find("\\end{" + env.command + "}", 6)
126 |         while 0 < i < j:  # in case the class is nested
127 |             i = env.source.text.find("\\begin{" + env.command + "}", i + 6)
128 |             j = env.source.text.find("\\end{" + env.command + "}", j + 6)
129 |         env.source.index += j + 5 + len(env.command)
130 |         env.clean.aggro.add("begin{" + env.command + "}")
131 | 


--------------------------------------------------------------------------------
/scr/exceptions/sub_begin/begin_custom.py:
--------------------------------------------------------------------------------
 1 | """custom begin routines"""
 2 | 
 3 | # ----------------------------------------
 4 | # FUNCTIONS
 5 | # ----------------------------------------
 6 | 
 7 | 
 8 | def _title(env) -> None:
 9 |     """add title to CLEAN"""
10 |     env.clean.add(env.command.title() + ".")
11 | 
12 | 
13 | def _thm(env) -> None:
14 |     """add theorem to CLEAN"""
15 |     env.clean.add("Theorem.")
16 | 
17 | 
18 | # ----------------------------------------
19 | # VARIABLES
20 | # ----------------------------------------
21 | 
22 | dic_commands_c = {
23 |     "assumption": _title,
24 |     "example": _title,
25 |     "exercise": _title,
26 |     "thm": _thm,
27 | }
28 | 
29 | void_c = ()
30 | 
31 | # TEMPLATE
32 | # dic_commands_c = {
33 | #     "{name_command}": {name_function},
34 | # }
35 | 


--------------------------------------------------------------------------------
/scr/exceptions/sub_end/__init__.py:
--------------------------------------------------------------------------------
 1 | """end routines module intitialiser"""
 2 | 
 3 | # ----------------------------------------
 4 | # BULTI-IN FUNCTIONS
 5 | # ----------------------------------------
 6 | 
 7 | 
 8 | def _proof(env) -> None:
 9 |     """add proof to CLEAN"""
10 |     env.clean.add("■\n")
11 | 
12 | 
13 | # ----------------------------------------
14 | # VARIABLES
15 | # ----------------------------------------
16 | 
17 | from .end_custom import void_c
18 | 
19 | # every end command is automatically void, void_c can be use to invalidate bulti-in end commands
20 | 
21 | from .end_custom import dic_commands_c
22 | 
23 | dic_commands = {"proof": _proof}
24 | 
25 | # ----------------------------------------
26 | # INTERPRETER
27 | # ----------------------------------------
28 | 
29 | 
30 | def interpret(env) -> None:
31 |     """custom interpreter for the end routine"""
32 |     if env.command in void_c:
33 |         pass
34 |     elif env.command in dic_commands_c:
35 |         dic_commands_c[env.command](env)
36 |     elif env.command in dic_commands:
37 |         dic_commands[env.command](env)
38 | 


--------------------------------------------------------------------------------
/scr/exceptions/sub_end/end_custom.py:
--------------------------------------------------------------------------------
 1 | """custom end routines"""
 2 | 
 3 | # ----------------------------------------
 4 | # FUNCTIONS
 5 | # ----------------------------------------
 6 | 
 7 | # ----------------------------------------
 8 | # VARIABLES
 9 | # ----------------------------------------
10 | 
11 | dic_commands_c = {"": lambda *args: None}
12 | 
13 | void_c = ()
14 | 
15 | # TEMPLATE
16 | # dic_commands_c = {
17 | #     "{name_command}": {name_function},
18 | # }
19 | 


--------------------------------------------------------------------------------
/scr/grammafy.py:
--------------------------------------------------------------------------------
  1 | """necessary modules"""
  2 | 
  3 | import os
  4 | import sys
  5 | import argparse
  6 | import re
  7 | from classes import Source, Clean
  8 | from exceptions import interpret
  9 | import pyle_manager  # type: ignore
 10 | 
 11 | 
 12 | class Environment:
 13 |     """class to hold the environement variables"""
 14 | 
 15 |     def __init__(self, file_path: str) -> None:
 16 |         with open(file_path, encoding="utf-8") as source_file:
 17 |             self.source = Source(source_file.read())
 18 |         self.clean = Clean()
 19 |         self.folder_path = f"{os.path.dirname(file_path)}{os.sep}"
 20 |         self.command = ""
 21 | 
 22 | 
 23 | def grammafy(file_path: str = "") -> None:
 24 |     """main function to execute"""
 25 | 
 26 |     if not file_path:
 27 |         input("Press enter to pick a tex file")
 28 |         file_path = pyle_manager.file_manager(True)
 29 | 
 30 |     file_name = ""
 31 |     if not file_path:
 32 |         sys.exit("File not selected")
 33 |     elif not file_path.endswith(".tex"):
 34 |         if (
 35 |             input(
 36 |                 "The file selected is not in a tex format, enter Y to continue anyway. "
 37 |             ).lower()
 38 |             != "y"
 39 |         ):
 40 |             sys.exit("Grammification interrupted")
 41 |         else:
 42 |             file_name = os.path.basename(file_path)
 43 |     else:
 44 |         file_name = os.path.basename(file_path)[:-4]
 45 | 
 46 |     if not file_name:
 47 |         sys.exit("Error fetching the file name")
 48 | 
 49 |     # list of admissible characters for commands
 50 |     end_command = (
 51 |         " ",
 52 |         "{",
 53 |         "}",
 54 |         ".",
 55 |         ",",
 56 |         ":",
 57 |         ";",
 58 |         "[",
 59 |         "]",
 60 |         "(",
 61 |         ")",
 62 |         "

quot;,
 63 |         "\\",
 64 |         "\n",
 65 |         '"',
 66 |         "'",
 67 |         "~",
 68 |     )
 69 | 
 70 |     env = Environment(file_path)
 71 | 
 72 |     # copy the main .tex file to a string
 73 | 
 74 |     # find the beginning of the document
 75 |     if "\\begin{document}" not in env.source.text:
 76 |         print("\\begin{document} missing")
 77 |     else:
 78 |         env.source.move_index("\\begin{document}")
 79 | 
 80 |     # start analysing the text
 81 |     while env.source.head:  # if any such element occurs
 82 |         next_index = env.source.inter
 83 |         if next_index == -1:
 84 |             env.clean.add(env.source.text)
 85 |             env.source.pop()
 86 |             continue
 87 | 
 88 |         # we can immediately add what we skipped before any interactive element
 89 |         env.clean.add(env.source.text[:next_index])
 90 |         env.source.index += next_index
 91 | 
 92 |         match env.source.text[0]:
 93 |             case "\\":  # FROM HERE - MAKE IT INTO A MATCH and include all this into the interpret if possible
 94 |                 i = min(
 95 |                     (
 96 |                         env.source.text.find(x, 1)
 97 |                         for x in end_command
 98 |                         if x in env.source.text[1:]
 99 |                     )
100 |                 )  # take note of the index of such element
101 |                 env.command = env.source.text[1:i]
102 |                 env.source.index += i
103 |                 # execute the routines
104 |                 interpret(env)
105 |             case "~":
106 |                 env.source.index += 1
107 |                 env.clean.add(" ")
108 |             case "{":
109 |                 env.source.index += 1
110 |             case "}":
111 |                 env.source.index += 1
112 |             case "

quot;:
113 |                 env.clean.add("[_]")
114 |                 env.source.index += 1
115 |                 if env.source.text[0] == "

quot;:
116 |                     env.source.move_index("$")
117 |                 else:  # assuming there are no double dollars within one-dollar equations
118 |                     env.source.move_index("

quot;)
119 |             case "%":
120 |                 env.source.move_index("\n")
121 |             case _:
122 |                 if (
123 |                     input(
124 |                         f"Fatal error, unknown interactive {env.source.text[0]}. \
125 |                         Press Y to continue or any other button to abort"
126 |                     ).lower()
127 |                     != "y"
128 |                 ):
129 |                     sys.exit("Aborted")
130 |                 else:
131 |                     env.source.index += 1
132 | 
133 |     # CLEANING ROUTINES
134 |     # trailing spaces
135 |     env.clean.text = env.clean.text.strip()
136 |     # unmatched brackets and tabs
137 |     env.clean.text = (
138 |         env.clean.text.replace("[]", "").replace("()", "").replace("\t", " ")
139 |     )
140 |     # pointless spaces
141 |     env.clean.text = re.sub(r"( )*\n( )*", "\n", env.clean.text)
142 |     # too many lines
143 |     env.clean.text = re.sub(r"\n\n\s*", "\n\n", env.clean.text)
144 |     # dourble spacing
145 |     env.clean.text = re.sub(r"( )+", " ", env.clean.text)
146 |     # remove new line before [_] unless preceded by -
147 |     env.clean.text = re.sub(r"(\S)\n?(?<!-)\[_\]", r"\1 [_]", env.clean.text)
148 |     # remove new line after [_] unless followed by bulletpoint
149 |     env.clean.text = re.sub(
150 |         r"\[_\](\.|,|;)?\n(?!(?:\d+\.|-))(\S)", r"[_]\1 \2", env.clean.text
151 |     )
152 | 
153 |     with open(
154 |         f"{env.folder_path}{file_name}_grammafied.txt", "w", encoding="utf-8"
155 |     ) as file_output:
156 |         file_output.write(env.clean.text)
157 |         print(
158 |             f"File written successfully, check {env.folder_path}{file_name}_grammafied.txt"
159 |         )
160 | 
161 |     if any(env.clean.aggro):
162 |         print(f"Unknown commands, please check {file_name}_unknowns.txt")
163 |         with open(
164 |             f"{env.folder_path}{file_name}_unknowns.txt", "w", encoding="utf-8"
165 |         ) as file_unknowns:
166 |             file_unknowns.write(str(env.clean.aggro))
167 | 
168 | 
169 | if __name__ == "__main__":
170 |     parser = argparse.ArgumentParser(prog="grammafy", description="clean up tex files")
171 |     parser.add_argument("-c", "--commandline", help="select via command line argument")
172 |     args = parser.parse_args()  # args.picker contains the modality
173 |     grammafy(args.commandline)
174 | 


--------------------------------------------------------------------------------
/scr/pyle_manager.py:
--------------------------------------------------------------------------------
  1 | """built-in cross-platform modules"""
  2 | 
  3 | import os
  4 | import time
  5 | import argparse
  6 | import ctypes
  7 | from itertools import chain
  8 | from platform import system
  9 | import unicurses as uc  # type: ignore
 10 | 
 11 | 
 12 | # mutable settings
 13 | class Settings:
 14 |     """class containing the global settings"""
 15 | 
 16 |     def __init__(self) -> None:
 17 |         # immutables
 18 |         self.file_size_vars = ("b", "kb", "mb", "gb")
 19 | 
 20 |         # mutable
 21 |         self.size = False
 22 |         self.time = False
 23 |         self.hidden = False
 24 |         self.beep = False
 25 |         self.permission = False
 26 |         self.order = 0
 27 | 
 28 |         # reset at each execution
 29 |         self.current_directory: list[str]
 30 |         self.start_line_directory: int
 31 |         self.selection: str
 32 |         self.index: int
 33 | 
 34 |         # init variables
 35 |         self.picker: bool
 36 |         self.local_folder: str
 37 | 
 38 |     def init(self, picker: bool) -> None:
 39 |         """initialise settings to the current session"""
 40 | 
 41 |         # reset at each different execution
 42 |         self.current_directory = []
 43 |         self.start_line_directory = 0
 44 |         self.selection = ""
 45 |         self.index = 0
 46 | 
 47 |         # init variables
 48 |         self.picker = picker
 49 |         self.local_folder = os.path.abspath(os.getcwd())
 50 |         uc.cbreak()
 51 |         uc.noecho()
 52 |         uc.keypad(uc.stdscr, True)
 53 |         uc.curs_set(0)
 54 |         uc.leaveok(uc.stdscr, True)
 55 | 
 56 |     @property
 57 |     def rows(self) -> int:
 58 |         """return rows length"""
 59 | 
 60 |         return uc.getmaxy(uc.stdscr)
 61 | 
 62 |     @property
 63 |     def cols(self) -> int:
 64 |         """return columns length"""
 65 | 
 66 |         return uc.getmaxx(uc.stdscr)
 67 | 
 68 |     def change_size(self) -> None:
 69 |         """toggle size"""
 70 | 
 71 |         self.size = not self.size
 72 | 
 73 |     def change_time(self) -> None:
 74 |         """toggle time"""
 75 | 
 76 |         self.time = not self.time
 77 | 
 78 |     def change_hidden(self) -> None:
 79 |         """toggle hidden"""
 80 | 
 81 |         self.hidden = not self.hidden
 82 | 
 83 |     def change_beep(self) -> None:
 84 |         """toggle beep"""
 85 | 
 86 |         self.beep = not self.beep
 87 | 
 88 |     def change_permission(self) -> None:
 89 |         """toggle permission"""
 90 | 
 91 |         self.permission = not self.permission
 92 | 
 93 |     def update_order(self, stay: bool) -> None:
 94 |         """update order, False stay, True move to the next entry"""
 95 | 
 96 |         old_order = self.order
 97 |         # create a vector with (1,a,b) where a,b are one if dimension and TIME_MODIFIED are enabled
 98 |         settings_enabled = (
 99 |             1,
100 |             self.size * any(os.path.isfile(x) for x in _directory()),
101 |             self.time,
102 |         )
103 |         # search the next 1 and if not found return 0
104 |         self.order = (
105 |             settings_enabled.index(1, self.order + stay)
106 |             if 1 in settings_enabled[self.order + stay :]
107 |             else 0
108 |         )
109 |         if self.order != old_order:
110 |             # only update if the previous order was changed
111 |             self.current_directory = []
112 | 
113 |     def update_selection(self) -> None:
114 |         """update the name of the selected folder"""
115 | 
116 |         if len(_directory()) > 0:
117 |             self.selection = _directory()[self.index]
118 | 
119 |     def quit(self) -> None:
120 |         """quitting routines"""
121 | 
122 |         os.chdir(self.local_folder)
123 |         uc.endwin()
124 | 
125 | 
126 | SETTINGS = Settings()
127 | 
128 | # --------------------------------------------------
129 | 
130 | 
131 | def _file_size(path: str) -> str:
132 |     """return file size as a formatted string"""
133 |     size = os.lstat(path).st_size
134 |     i = len(str(size)) // 3
135 |     if len(str(size)) % 3 == 0:
136 |         i -= 1
137 |     if i > 3:
138 |         i = 3
139 |     display_size = size / 1000**i
140 |     return f"{display_size:.2f}{SETTINGS.file_size_vars[i]}"
141 | 
142 | 
143 | def _directory() -> list[str]:
144 |     """list of folders and files"""
145 |     # return the previous value if exists
146 |     if not SETTINGS.current_directory:
147 |         directories = os.listdir()
148 |         # order by
149 |         match SETTINGS.order:
150 |             # size
151 |             case 1:
152 |                 dirs = chain(
153 |                     sorted(
154 |                         (
155 |                             x
156 |                             for x in directories
157 |                             if os.path.isdir(x)
158 |                             and (SETTINGS.hidden or not x.startswith("."))
159 |                         ),
160 |                         key=lambda x: os.lstat(x).st_size,
161 |                     ),
162 |                     sorted(
163 |                         (
164 |                             x
165 |                             for x in directories
166 |                             if os.path.isfile(x)
167 |                             and (SETTINGS.hidden or not x.startswith("."))
168 |                         ),
169 |                         key=lambda x: os.lstat(x).st_size,
170 |                     ),
171 |                 )
172 |             # time modified
173 |             case 2:
174 |                 dirs = chain(
175 |                     sorted(
176 |                         (
177 |                             x
178 |                             for x in directories
179 |                             if os.path.isdir(x)
180 |                             and (SETTINGS.hidden or not x.startswith("."))
181 |                         ),
182 |                         key=lambda x: os.lstat(x).st_mtime,
183 |                     ),
184 |                     sorted(
185 |                         (
186 |                             x
187 |                             for x in directories
188 |                             if os.path.isfile(x)
189 |                             and (SETTINGS.hidden or not x.startswith("."))
190 |                         ),
191 |                         key=lambda x: os.lstat(x).st_mtime,
192 |                     ),
193 |                 )
194 |             # name
195 |             case _:  # 0 or unrecognised values
196 |                 dirs = chain(
197 |                     sorted(
198 |                         (
199 |                             x
200 |                             for x in directories
201 |                             if os.path.isdir(x)
202 |                             and (SETTINGS.hidden or not x.startswith("."))
203 |                         ),
204 |                         key=lambda s: s.lower(),
205 |                     ),
206 |                     sorted(
207 |                         (
208 |                             x
209 |                             for x in directories
210 |                             if os.path.isfile(x)
211 |                             and (SETTINGS.hidden or not x.startswith("."))
212 |                         ),
213 |                         key=lambda s: s.lower(),
214 |                     ),
215 |                 )
216 |         SETTINGS.current_directory = list(dirs)
217 |     return SETTINGS.current_directory
218 | 
219 | 
220 | def _print_line(line_num: int, k: int, l_size: int) -> None:
221 |     x = _directory()[k]
222 |     if os.path.isdir(x):
223 |         uc.mvaddch(3 + line_num, 1, "<")
224 | 
225 |     # add extensions
226 |     columns_count = 0
227 |     if SETTINGS.permission and SETTINGS.cols - columns_count - 9 + 1 >= 8:
228 |         columns_count += 9
229 |         uc.mvaddstr(
230 |             3 + line_num,
231 |             SETTINGS.cols - columns_count + 1,
232 |             "| "
233 |             + ("r " if os.access(x, os.R_OK) else "- ")
234 |             + ("w " if os.access(x, os.W_OK) else "- ")
235 |             + ("x" if os.access(x, os.X_OK) else "-"),
236 |         )
237 |     if SETTINGS.time and SETTINGS.cols - columns_count - 22 + 1 >= 8:
238 |         columns_count += 22
239 |         uc.mvaddstr(
240 |             3 + line_num,
241 |             SETTINGS.cols - columns_count + 1,
242 |             "| "
243 |             + time.strftime(
244 |                 "%Y-%m-%d %H:%M:%S",
245 |                 time.strptime(time.ctime(os.lstat(x).st_mtime)),
246 |             ),
247 |         )
248 |     if (
249 |         SETTINGS.size
250 |         and os.path.isfile(x)
251 |         and SETTINGS.cols - columns_count - 3 - l_size + 1 >= 8
252 |     ):
253 |         columns_count += 3 + l_size
254 |         uc.mvaddstr(
255 |             3 + line_num,
256 |             SETTINGS.cols - columns_count + 1,
257 |             "| " + _file_size(x),
258 |         )
259 |     if len(x) > SETTINGS.cols - 2 - columns_count:
260 |         name_x = "... " + x[-(SETTINGS.cols - 6 - columns_count) :]
261 |     else:
262 |         name_x = x
263 |     uc.mvaddwstr(3 + line_num, 2, name_x)
264 | 
265 | 
266 | def _dir_printer(refresh: bool = False, position: str = "beginning") -> None:
267 |     """printing function"""
268 | 
269 |     # check positions and fix index accordingly
270 |     if refresh:
271 |         SETTINGS.current_directory = []
272 |         SETTINGS.start_line_directory = 0
273 | 
274 |     # init vars
275 |     l_size = max((len(_file_size(x)) for x in _directory())) if _directory() else 0
276 | 
277 |     if position == "beginning":
278 |         SETTINGS.start_line_directory = 0
279 |         SETTINGS.index = 0
280 | 
281 |     elif position == "selection":
282 |         if SETTINGS.selection in _directory():
283 |             SETTINGS.index = _directory().index(SETTINGS.selection)
284 |         else:
285 |             SETTINGS.index = 0
286 |         # correct in case we go out of monitor
287 |         SETTINGS.start_line_directory = max(0, 4 + SETTINGS.index - SETTINGS.rows)
288 |         position = "index"
289 | 
290 |     elif position == "up":
291 |         SETTINGS.index -= 1
292 |         if SETTINGS.index >= SETTINGS.start_line_directory:
293 |             uc.mvaddch(3 + SETTINGS.index - SETTINGS.start_line_directory + 1, 0, " ")
294 |             uc.mvaddch(3 + SETTINGS.index - SETTINGS.start_line_directory, 0, "-")
295 | 
296 |         else:
297 |             # else print up one
298 |             SETTINGS.start_line_directory -= 1
299 | 
300 |             uc.move(3, 0)
301 |             uc.insertln()
302 | 
303 |             _print_line(0, SETTINGS.start_line_directory, l_size)
304 |             uc.mvaddch(4, 0, " ")
305 |             uc.mvaddch(3, 0, "-")
306 |         return
307 | 
308 |     elif position == "down":
309 |         SETTINGS.index += 1
310 |         if SETTINGS.index < SETTINGS.rows - 3 + SETTINGS.start_line_directory:
311 |             uc.mvaddch(3 + SETTINGS.index - SETTINGS.start_line_directory - 1, 0, " ")
312 |             uc.mvaddch(3 + SETTINGS.index - SETTINGS.start_line_directory, 0, "-")
313 | 
314 |         else:
315 |             # else print down 1
316 | 
317 |             uc.move(3, 0)
318 |             uc.deleteln()
319 | 
320 |             max_line = min(
321 |                 len(_directory()),
322 |                 SETTINGS.start_line_directory + SETTINGS.rows - 3,
323 |             )
324 | 
325 |             SETTINGS.start_line_directory += 1
326 | 
327 |             _print_line(SETTINGS.rows - 4, max_line, l_size)
328 |             uc.mvaddch(SETTINGS.rows - 2, 0, " ")
329 |             uc.mvaddch(SETTINGS.rows - 1, 0, "-")
330 |         return
331 | 
332 |     max_line = min(
333 |         len(_directory()),
334 |         SETTINGS.start_line_directory + SETTINGS.rows - 3,
335 |     )
336 | 
337 |     # print on screen
338 |     uc.clear()
339 | 
340 |     # path directory
341 |     uc.mvaddstr(0, 0, "# pyleManager --- press i for instructions #"[: SETTINGS.cols])
342 |     # name folder
343 |     name_folder = (
344 |         "... " if len(os.path.abspath(os.getcwd())) > SETTINGS.cols else ""
345 |     ) + os.path.abspath(os.getcwd())[5 - SETTINGS.cols :]
346 |     if not name_folder.endswith(os.sep):
347 |         name_folder += os.sep
348 |     uc.mvaddwstr(1, 0, name_folder)
349 | 
350 |     # folders and pointer
351 |     if len(_directory()) == 0:
352 |         uc.mvaddstr(2, 1, "**EMPTY FOLDER**")
353 |         position = ""
354 |         return
355 | 
356 |     SETTINGS.update_order(False)
357 | 
358 |     # write the description on top
359 |     columns_count = 0
360 |     uc.mvaddstr(2, 1, "v*NAME*" if SETTINGS.order == 0 else " *NAME*")
361 |     if SETTINGS.permission and SETTINGS.cols - columns_count - 9 + 1 >= 8:
362 |         columns_count += 9
363 |         uc.mvaddstr(2, SETTINGS.cols - columns_count + 1, ("| *PERM*"))
364 |     if SETTINGS.time and SETTINGS.cols - columns_count - 22 + 1 >= 8:
365 |         columns_count += 22
366 |         uc.mvaddstr(
367 |             2,
368 |             SETTINGS.cols - columns_count + 1,
369 |             ("|v" if SETTINGS.order == 2 else "| ") + "*TIME MODIFIED*",
370 |         )
371 |     if (
372 |         SETTINGS.size
373 |         and any(os.path.isfile(x) for x in _directory())
374 |         and SETTINGS.cols - columns_count - 3 - l_size + 1 >= 8
375 |     ):
376 |         columns_count += 3 + l_size
377 |         uc.mvaddstr(
378 |             2,
379 |             SETTINGS.cols - columns_count + 1,
380 |             ("|v" if SETTINGS.order == 1 else "| ") + "*SIZE*",
381 |         )
382 | 
383 |     if position == "index":
384 |         if len(_directory()) - 1 < SETTINGS.index:
385 |             SETTINGS.index = len(_directory()) - 1
386 |         if SETTINGS.index >= SETTINGS.rows - 3:
387 |             SETTINGS.start_line_directory = SETTINGS.index - (SETTINGS.rows - 3) + 1
388 | 
389 |     for line_num, k in enumerate(
390 |         range(
391 |             SETTINGS.start_line_directory,
392 |             max_line,
393 |         )
394 |     ):
395 |         _print_line(line_num, k, l_size)
396 | 
397 |     if position == "beginning":
398 |         uc.mvaddch(3, 0, "-")
399 |     elif position == "index":
400 |         uc.mvaddch(SETTINGS.index - SETTINGS.start_line_directory + 3, 0, "-")
401 | 
402 | 
403 | def _beeper() -> None:
404 |     """make a beep"""
405 |     if SETTINGS.beep:
406 |         uc.beep()
407 | 
408 | 
409 | def _instructions() -> None:
410 |     """print instructions"""
411 | 
412 |     uc.clear()
413 | 
414 |     lines = [
415 |         "INSTRUCTIONS:",
416 |         "",
417 |         'the prefix "<" means folder',
418 |         "",
419 |         "upqArrow = up",
420 |         "downArrow = down",
421 |         "r = refresh",
422 |         f"h = ({'yes' if SETTINGS.hidden else 'no'}) toggle hidden files",
423 |         f"d = ({'yes' if SETTINGS.size else 'no'}) toggle file size",
424 |         f"t = ({'yes' if SETTINGS.time else 'no'}) toggle time last modified",
425 |         f"b = ({'yes' if SETTINGS.beep else 'no'}) toggle beep",
426 |         f"p = ({'yes' if SETTINGS.permission else 'no'}) toggle permission"
427 |         f"m = ({('NAME', 'SIZE', 'TIME MODIFIED')[SETTINGS.order]}) change ordering"
428 |         f"enter = {'select file' if SETTINGS.picker else 'open using the default application launcher'}",
429 |         f"e = {'--disabled--' if SETTINGS.picker else 'edit using command-line editor'}"
430 |         "",
431 |         " -press q to quit-",
432 |     ]
433 |     nlines = len(lines)
434 |     start_line = 0
435 |     end_line = min(SETTINGS.rows - 1, nlines - 1)
436 | 
437 |     for i in range(start_line, end_line + 1):
438 |         uc.mvaddstr(i, 0, lines[i])
439 | 
440 |     while True:
441 |         button = uc.getkey()
442 |         if button == "q":
443 |             break
444 |         elif button == "KEY_UP":
445 |             if start_line > 0:
446 |                 start_line -= 1
447 |                 end_line -= 1
448 |                 uc.move(0, 0)
449 |                 uc.insertln()
450 |                 uc.mvaddstr(0, 0, lines[start_line])
451 |         elif button == "KEY_DOWN":
452 |             if end_line < nlines - 1:
453 |                 start_line += 1
454 |                 end_line += 1
455 |                 uc.move(0, 0)
456 |                 uc.deleteln()
457 |                 uc.mvaddstr(SETTINGS.rows - 1, 0, lines[end_line])
458 | 
459 | 
460 | # --------------------------------------------------
461 | 
462 | 
463 | def _file_manager(stdscr: ctypes.c_void_p, picker: bool) -> str:
464 |     """file manager, wrapped by unicurses"""
465 | 
466 |     SETTINGS.init(picker)
467 | 
468 |     while SETTINGS.rows < 4 or SETTINGS.cols < 8:
469 |         uc.mvaddstr(0, 0, "RESIZE")
470 |         uc.getkey()
471 | 
472 |     _dir_printer(refresh=True, position="beginning")
473 | 
474 |     output = ""
475 | 
476 |     while True:
477 |         SETTINGS.update_selection()
478 | 
479 |         match uc.getkey():
480 |             # up
481 |             case "KEY_UP":
482 |                 if len(_directory()) > 0 and SETTINGS.index > 0:
483 |                     _dir_printer(position="up")
484 |                 else:
485 |                     _beeper()
486 | 
487 |             # down
488 |             case "KEY_DOWN":
489 |                 if len(_directory()) > 0 and SETTINGS.index < len(_directory()) - 1:
490 |                     _dir_printer(position="down")
491 |                 else:
492 |                     _beeper()
493 | 
494 |             # right
495 |             case "KEY_RIGHT":
496 |                 if (
497 |                     len(_directory()) > 0
498 |                     and os.path.isdir(SETTINGS.selection)
499 |                     and os.access(SETTINGS.selection, os.R_OK)
500 |                 ):
501 |                     os.chdir(SETTINGS.selection)
502 |                     _dir_printer(refresh=True, position="beginning")
503 |                 else:
504 |                     _beeper()
505 | 
506 |             # left
507 |             case "KEY_LEFT":
508 |                 if os.path.dirname(os.getcwd()) != os.getcwd():
509 |                     os.chdir("..")
510 |                     _dir_printer(refresh=True, position="beginning")
511 |                 else:
512 |                     _beeper()
513 | 
514 |             # quit
515 |             case "q":
516 |                 break
517 | 
518 |             # refresh
519 |             case "r":
520 |                 _dir_printer(refresh=True, position="selection")
521 | 
522 |             # toggle hidden
523 |             case "h":
524 |                 SETTINGS.change_hidden()
525 |                 _dir_printer(refresh=True, position="selection")
526 | 
527 |             # size
528 |             case "d":
529 |                 SETTINGS.change_size()
530 |                 _dir_printer(position="selection")
531 | 
532 |             # time
533 |             case "t":
534 |                 SETTINGS.change_time()
535 |                 _dir_printer(position="selection")
536 | 
537 |             # beep
538 |             case "b":
539 |                 SETTINGS.change_beep()
540 | 
541 |             # permission
542 |             case "p":
543 |                 SETTINGS.change_permission()
544 |                 _dir_printer(position="selection")
545 | 
546 |             # change order
547 |             case "m":
548 |                 SETTINGS.update_order(True)
549 |                 _dir_printer(position="selection")
550 | 
551 |             # enter
552 |             case "^J":
553 |                 if len(_directory()) > 0:
554 |                     if SETTINGS.picker:
555 |                         path = os.path.join(os.getcwd(), SETTINGS.selection)
556 |                         output = path
557 |                         break
558 | 
559 |                     elif not SETTINGS.picker:
560 |                         selection_os = SETTINGS.selection.replace('"', '\\"')
561 |                         match system():
562 |                             case "Linux":
563 |                                 os.system(f'xdg-open "{selection_os}"')
564 |                             case "Windows":
565 |                                 os.system(selection_os)
566 |                             case "Darwin":
567 |                                 os.system(f'open "{selection_os}"')
568 |                             case _:
569 |                                 uc.clear()
570 |                                 uc.mvaddstr(
571 |                                     0,
572 |                                     0,
573 |                                     "System not recognised, press any button to continue",
574 |                                 )
575 |                                 uc.getkey()
576 |                                 _dir_printer(position="selection")
577 |                 else:
578 |                     _beeper()
579 | 
580 |             # command-line editor
581 |             case "e":
582 |                 if len(_directory()) > 0 and not SETTINGS.picker:
583 |                     selection_os = SETTINGS.selection.replace('"', '\\"')
584 |                     match system():
585 |                         case "Linux":
586 |                             os.system(f'$EDITOR "{selection_os}"')
587 |                         case "Windows":
588 |                             uc.clear()
589 |                             uc.mvaddstr(
590 |                                 0,
591 |                                 0,
592 |                                 "Windows does not have any built-in command line editor, press any button to continue",
593 |                             )
594 |                             uc.getkey()
595 |                             _dir_printer(position="selection")
596 |                         case "Darwin":
597 |                             os.system(f'open -e "{selection_os}"')
598 |                         case _:
599 |                             uc.clear()
600 |                             uc.mvaddstr(
601 |                                 0,
602 |                                 0,
603 |                                 "System not recognised, press any button to continue",
604 |                             )
605 |                             uc.getkey()
606 |                             _dir_printer(position="selection")
607 |                 else:
608 |                     _beeper()
609 | 
610 |             # instructions
611 |             case "i":
612 |                 _instructions()
613 |                 _dir_printer(position="selection")
614 | 
615 |             case "KEY_RESIZE":
616 |                 if SETTINGS.rows < 4 or SETTINGS.cols < 8:
617 |                     uc.clear()
618 |                     uc.mvaddstr(0, 0, "RESIZE")
619 |                 else:
620 |                     _dir_printer(position="selection")
621 | 
622 |             case _:
623 |                 pass
624 | 
625 |     SETTINGS.quit()
626 | 
627 |     return output
628 | 
629 | 
630 | def file_manager(picker: bool = False) -> str:
631 |     """file manager"""
632 | 
633 |     return uc.wrapper(_file_manager, picker)
634 | 
635 | 
636 | if __name__ == "__main__":
637 |     # parsing args
638 |     parser = argparse.ArgumentParser(
639 |         prog="pyleManager", description="file manager written in Python"
640 |     )
641 |     parser.add_argument(
642 |         "-p", "--picker", action="store_true", help="use pyleManager as a file selector"
643 |     )
644 |     args = parser.parse_args()  # args.picker contains the modality
645 | 
646 |     file_manager(args.picker)
647 | 


--------------------------------------------------------------------------------

