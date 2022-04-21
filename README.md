# pyfastspring

This is a simple Python module designed to interact with the FastSpring ordering
and subscription API. This is based on the Artlogic [fastspring][1] repository, which was 
FastSpring's "Classic" (XML-based) API and contained both Python2 and 3 versions. 

This is for Python3 only, and is for FastSpring's (JSON) API.

This module requires `requests` to work. Data is passed into and returned from the API object in dicts.

## Methods

Each method of the API class corresponds directly to an API endpoint. The
[official FastSpring API documentation][2] is the best reference for
understanding what does what. 

[1]: https://github.com/artlogicmedia/fastspring/
[2]: https://developer.fastspring.com/reference/getting-started-with-your-api
