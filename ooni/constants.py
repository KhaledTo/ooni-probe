CANONICAL_BOUNCER_ONION = 'httpo://nkvphnp3p6agi5qq.onion'
# XXX Change these two to the production ones once the release is made.
# CANONICAL_BOUNCER_HTTPS = 'https://bouncer.ooni.io'
CANONICAL_BOUNCER_HTTPS = 'https://bouncer.test.ooni.io'
CANONICAL_BOUNCER_CLOUDFRONT = (
    'https://d3kr4emv7f56qa.cloudfront.net/',
    'a0.awsstatic.com'
)

MEEK_BRIDGES = [
    ("meek 0.0.2.0:2 B9E7141C594AF25699E0079C1F0146F409495296 "
     "url=https://d2zfqthxsdq309.cloudfront.net/ front=a0.awsstatic.com"),
    ("meek 0.0.2.0:3 A2C13B7DFCAB1CBF3A884B6EB99A98067AB6EF44 "
     "url=https://az786092.vo.msecnd.net/ front=ajax.aspnetcdn.com")
]

# These are bridges taken from TBB
OBFS4_BRIDGES = [
    ("obfs4 154.35.22.10:41835 8FB9F4319E89E5C6223052AA525A192AFBC85D55 "
     "cert=GGGS1TX4R81m3r0HBl79wKy1OtPPNR2CZUIrHjkRg65Vc2VR8fOyo64f9kmT1UAFG7j0HQ iat-mode=0"),

    ("obfs4 198.245.60.50:443 752CF7825B3B9EA6A98C83AC41F7099D67007EA5 "
     "cert=xpmQtKUqQ/6v5X7ijgYE/f03+l2/EuQ1dexjyUhh16wQlu"
     "/cpXUGalmhDIlhuiQPNEKmKw iat-mode=0"),

    ("obfs4 192.99.11.54:443 7B126FAB960E5AC6A629C729434FF84FB5074EC2 "
     "cert=VW5f8+IBUWpPFxF+rsiVy2wXkyTQG7vEd"
     "+rHeN2jV5LIDNu8wMNEOqZXPwHdwMVEBdqXEw iat-mode=0"),

    ("obfs4 109.105.109.165:10527 8DFCD8FB3285E855F5A55EDDA35696C743ABFC4E "
     "cert=Bvg/itxeL4TWKLP6N1MaQzSOC6tcRIBv6q57DYAZc3b2AzuM"
     "+/TfB7mqTFEfXILCjEwzVA iat-mode=0"),

    ("obfs4 83.212.101.3:41213 A09D536DD1752D542E1FBB3C9CE4449D51298239 "
     "cert=lPRQ/MXdD1t5SRZ9MquYQNT9m5DV757jtdXdlePmRCudUU9CFUOX1Tm7"
     "/meFSyPOsud7Cw iat-mode=0"),

    ("obfs4 104.131.108.182:56880 EF577C30B9F788B0E1801CF7E433B3B77792B77A "
     "cert=0SFhfDQrKjUJP8Qq6wrwSICEPf3Vl"
     "/nJRsYxWbg3QRoSqhl2EB78MPS2lQxbXY4EW1wwXA iat-mode=0"),

    ("obfs4 109.105.109.147:13764 BBB28DF0F201E706BE564EFE690FE9577DD8386D "
     "cert=KfMQN/tNMFdda61hMgpiMI7pbwU1T+wxjTulYnfw"
     "+4sgvG0zSH7N7fwT10BI8MUdAD7iJA iat-mode=0"),

    ("obfs4 154.35.22.11:49868 A832D176ECD5C7C6B58825AE22FC4C90FA249637 "
     "cert=YPbQqXPiqTUBfjGFLpm9JYEFTBvnzEJDKJxXG5Sxzrr"
     "/v2qrhGU4Jls9lHjLAhqpXaEfZw iat-mode=0"),

    ("obfs4 154.35.22.12:80 00DC6C4FA49A65BD1472993CF6730D54F11E0DBB "
      "cert=N86E9hKXXXVz6G7w2z8wFfhIDztDAzZ"
     "/3poxVePHEYjbKDWzjkRDccFMAnhK75fc65pYSg iat-mode=0"),

    ("obfs4 154.35.22.13:443 FE7840FE1E21FE0A0639ED176EDA00A3ECA1E34D "
      "cert=fKnzxr+m+jWXXQGCaXe4f2gGoPXMzbL+bTBbXMYXuK0tMotd"
     "+nXyS33y2mONZWU29l81CA iat-mode=0"),

    ("obfs4 154.35.22.10:80 8FB9F4319E89E5C6223052AA525A192AFBC85D55 "
      "cert=GGGS1TX4R81m3r0HBl79wKy1OtPPNR2CZUIrHjkRg65Vc2VR8fOyo64f9kmT1UAFG7j0HQ iat-mode=0"),

    ("obfs4 154.35.22.10:443 8FB9F4319E89E5C6223052AA525A192AFBC85D55 "
      "cert=GGGS1TX4R81m3r0HBl79wKy1OtPPNR2CZUIrHjkRg65Vc2VR8fOyo64f9kmT1UAFG7j0HQ iat-mode=0"),

    ("obfs4 154.35.22.11:443 A832D176ECD5C7C6B58825AE22FC4C90FA249637 "
     "cert=YPbQqXPiqTUBfjGFLpm9JYEFTBvnzEJDKJxXG5Sxzrr"
     "/v2qrhGU4Jls9lHjLAhqpXaEfZw iat-mode=0"),

    ("obfs4 154.35.22.11:80 A832D176ECD5C7C6B58825AE22FC4C90FA249637 "
     "cert=YPbQqXPiqTUBfjGFLpm9JYEFTBvnzEJDKJxXG5Sxzrr"
     "/v2qrhGU4Jls9lHjLAhqpXaEfZw iat-mode=0"),

    ("obfs4 154.35.22.9:60873 C73ADBAC8ADFDBF0FC0F3F4E8091C0107D093716 "
     "cert=gEGKc5WN/bSjFa6UkG9hOcft1tuK"
     "+cV8hbZ0H6cqXiMPLqSbCh2Q3PHe5OOr6oMVORhoJA iat-mode=0"),

    ("obfs4 154.35.22.9:80 C73ADBAC8ADFDBF0FC0F3F4E8091C0107D093716 "
     "cert=gEGKc5WN/bSjFa6UkG9hOcft1tuK"
     "+cV8hbZ0H6cqXiMPLqSbCh2Q3PHe5OOr6oMVORhoJA iat-mode=0"),

    ("obfs4 154.35.22.9:443 C73ADBAC8ADFDBF0FC0F3F4E8091C0107D093716 "
     "cert=gEGKc5WN/bSjFa6UkG9hOcft1tuK"
     "+cV8hbZ0H6cqXiMPLqSbCh2Q3PHe5OOr6oMVORhoJA iat-mode=0")
]
