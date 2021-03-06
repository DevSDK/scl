# SCL (Seokho's CheckList)

This is a simple checklist generator to your notion.

![Screenshot from 2021-03-06 12-02-52](https://user-images.githubusercontent.com/18409763/110192855-09c2ce80-7e74-11eb-8f81-8fa3b6ef37fc.png)


### How to use
```shell
    pip3 install notion
```
**Attention!**: There are some issue in notion library. You should change limits in library source codes. See [this issue](https://github.com/jamalex/notion-py/issues/292#issuecomment-791053675).

And you can run
```shell
    python3 scl.py
```

Then you can found 'config.json' in scl.py locationed directory.
```json
    {
        "Auth": "", 
        "Page": ""
    }
```

**Auth** Required your notion token. Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so

**Page**  is a target page id. you can paste just URL or id

Now you can use
```shell
    python3 scl.py
```

### Add checklist set

You can add your own checklist in checklist.json.

```json
{
    "commit": [
        "No missing files"
    ],
    "another": [
        "check domain"
    ]
}
```