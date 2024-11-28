Title: Your Python smells like Java
Slug: your-python-smells-like-java

Whether you like it or not, you already use different languages each day: SQL, Javascript, Python, C++ & more. Wisdom goes that learning different programming languages will help you become a better programmer, but many programmers don't get this benefit & feel that it's a waste of time. After talking & working with many of them for many years, I found out that they learn the _syntax_ of the language, maybe some libraries, but they don't learn the soul of the language.

### Examples
```python
# Bad: you need to read to the end to know the code intention
img.find('.jpg') != -1
img.find('.jpg') >= 0

# Good.Easier to read
'.jpg' in img
'.jpg' not in img
```

```python
# Bad. Hard-coded number
img[-4:] == '.jpg'

# Good. Works with any string of any length
img.endswith('.jpg')
```

```python
# Bad
(img.endswith('.jpg') or 
    img.endswith('.jpeg') or
    img.endswith('.png') or 
    img.endswith('.gif'))

# Good: uses python built-in capabilities to make code more compact
img.endswith((".jpg", ".jpeg", ".png", ".gif"))
```

```python
# Bad
(path == 'js' or 
    path == 'css' or 
    path == 'img' or
    path == 'font' or
    path == 'fonts')

# Good. Compact code.
path in ('js', 'css', 'img', 'font', 'fonts')
```

```python
# Bad
(os.path.exists(os.path.join(path, "space")) or 
    os.path.exists(os.path.join(path, "bucket")) or 
    os.path.exists(os.path.join(path, "actor")))

# Good. Compact code. Reads better. 
# The list can be moved to a different file
any(
    os.path.exists(os.path.join(path, item)) 
    for item in ["space", "bucket", "actor"])
```

```python
# Bad
for i in range(len(lst)):
    elt = lst[i]
    print i, elt

# Good. Uses built-in python functions
for i, elt in enumerate(lst):
    print i, elt
```

```python
# Bad
print 'Hello ', name, '. You are ', age, ' years old'

# Good. Reflects the structure of the intended output
print 'Hello {name}. You are {age} years old'.format(name=name, age=age)
```

```python
# Bad
if not (key in dict):
    print 'Key missing'

# Good. Reads better
if key not in dict:
    print 'Key missing'
```

```python
# Bad
s = names[0]
for name in names[1:]:
    s += ', ' + name

# Good. Doesn't have the off-by-one issues. Also faster
s = ', '.join(names)
```

```python
# Bad
# Find if array1 is a subset of array2
is_subset = True
for x in array1:
    found = False
    for y in array2:
        if x == y:
            found = True
            break

    if not found:
        is_subset = False
        break

# Good. 2 lines instead of 10!
def subset_of(array1, array2):
    return set(array1).issubset(array2)
```

```python
# Bad 
if case_sensitivity.lower() == 'sensitive':
    matcher = fnmatch.fnmatchcase
elif case_sensitivity.lower() == 'insensitive':
    def matcher(fname, pattern):
        return fnmatch.fnmatchcase(fname.lower(), pattern.lower())
else:
    matcher = fnmatch.fnmatch

# Good. The match code can be moved to a different file
matchers = {
'sensitive': fnmatch.fnmatchcase
'insensitive': lambda fname, pattern: fnmatch.fnmatchcase(fname.lower(), pattern.lower())
}.get(case_sensitivity.lower(), fnmatch.fnmatch)
```

### Read more

*   [Transforming code into beautiful idiomatic python by Raymond Hettinger](https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1)
*   [Why is Python more fun than Java?](http://brizzled.clapper.org/blog/2008/07/28/why-is-python-more-fun-than-java/)
*   [Python Is Not Java](http://dirtsimple.org/2004/12/python-is-not-java.html)
*   [Why I prefer Python to Java](http://thebuild.com/blog/2014/10/22/why-i-prefer-python-to-java-in-two-code-samples/)
