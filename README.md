# Invalid cookies in Cookie header

## Behaviour not specified for Invalid cookies in the Cookie header
The Cookie header format is specified in [RFC 6265, section 4.2.1](https://tools.ietf.org/html/rfc6265#section-4.2.1):

```BNF
cookie-header = "Cookie:" OWS cookie-string OWS
cookie-string = cookie-pair *( ";" SP cookie-pair )
```

The individual cookies are clearly delimited by semi-colons, but it is not specified what servers should do when receiving invalid strings between semi-colons.

### Examples
#### All RFC compliant cookies
`Cookie: SID=31d4d96e407aad42; lang=en-US`

#### Invalid cookie in the header
`Cookie: SID=31d4d96e407aad42; muffin ; lang=en-US`


## History
This repo started as part of a discussion for a Pull Request to the [Rust http library, Rust](https://github.com/hyperium/hyper). [Pull Request #1159](https://github.com/hyperium/hyper/pull/1159) was created in order to change its behaviour from:

* discarding the entire "Cookie header"
* ignore the last cookie in the header if terminated by a semi-colon

to:

* accept all valid individual cookies within the header, discarding any invalid string between any set of two semi-colon
* accept the last cookie in the header, regardless of being terminated by a semi-colon or not

The latter follows [Postel](https://en.wikipedia.org/wiki/Jon_Postel)'s law, the [Robustness principle](https://en.wikipedia.org/wiki/Robustness_principle)": "Be conservative in what you send, be liberal in what you accept". Cookies are often injected, therefore added to an existing header in most cases, by intermediary apps servers, security appliances, network devices, proxies, Load Balnacers etc... between the User-Agent and the server. Bugs in any one of these intermediates could inject an invalid cookie. The former behaviour leads to the entire Cookie header to be discarded. 

## Goal
The goal of this survey is to list the behaviours of how well-known Web Application Servers and libraries when receiving a Cookie header containing a mixture of valie and invalid coookies.

## How to crontribute
Provide a minimalist example of code using your favourite library which demonstrates its behaviour Be conservative in what you send, be liberal in what you accept, and add the result to this file.

### Testing
Send a request with an invalid cookie between two valid cookies, and one request with only valid cookies but terminated with a semi-colon:

* ending with a semi-column: `curl -b 'SID=31d4d96e407aad42; lang=en-US;' localhost:8080`
* invalid cookie: `curl -b 'SID=31d4d96e407aad42; muffin ; lang=en-US;' localhost:8080`
* invalid cookies with spaces: `curl -b 'SID=31d4d96e407aad42; muffin crumpet cupcake  ; lang=en-US;' localhost:8080`

## List of servers, libraries and results

Use a checkmark ✓ if the issues are just ignored and the valid cookies are made available, and a crossmark ✗ is the entire header is discarded (no cookie available).

| server/library | language | ending w/ ; | invalid cookie | invalid cookie with spaces  | comments
|---|:---:|:---:|:---:|:---:|---|
| [pure go](/pure_go) | golang |✓|✓|✓| Does not discard, assumes K/V pairs and adds an empty value to the invalid cookie value: `[SID=31d4d96e407aad42 lang=en-US][SID=31d4d96e407aad42 muffin= lang=en-US]`|
| [gorilla go](/gorilla_go) | golang |✓|✓|✓| same as pure_go|
| [express](/exress) | javascrit |✓|✓|✓|Systematically drops invalid cookies |
| [bottlepy](/bottlepy) | python |✓|✗|✗| Discards the entire header |
| [Flask](/flask) | python |✓|✗|✗| Does not discard, but munges the bad and good cookie together: `{'SID': '31d4d96e407aad42', 'muffin ; lang': 'en-US'}`|
| [ring](/ring/cookies) | clojure |✓|✓|✓| Discards invalid values `{SID {:value 31d4d96e407aad42}, lang {:value en-US}}` |
| example for copy/paste |✓✗|✓✗|✓✗|✓✗| |

