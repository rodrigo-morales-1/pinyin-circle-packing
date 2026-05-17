# import libraries
import circlify
import matplotlib.pyplot as plt
import os

plt.rcParams["font.family"] = "Noto Serif CJK SC"

data = [
    {
        "id": "root",
        "datum": 1,
        "children": [
            {
                "id": "yi",
                "datum": 1,
                "children": [
                    {
                        "id": "yī",
                        "datum": 1,
                        "children": [
                            {
                                "id": "一",
                                "datum": 1
                            },
                            {
                                "id": "伊",
                                "datum": 1
                            },
                            {
                                "id": "衣",
                                "datum": 1
                            },
                            {
                                "id": "医",
                                "datum": 1
                            },
                            {
                                "id": "依",
                                "datum": 1
                            },
                            {
                                "id": "壹",
                                "datum": 1
                            },
                            {
                                "id": "椅",
                                "datum": 1
                            },
                            {
                                "id": "祎",
                                "datum": 1
                            },
                            {
                                "id": "咿",
                                "datum": 1
                            },
                            {
                                "id": "铱",
                                "datum": 1
                            },
                            {
                                "id": "猗",
                                "datum": 1
                            },
                            {
                                "id": "揖",
                                "datum": 1
                            },
                            {
                                "id": "漪",
                                "datum": 1
                            },
                            {
                                "id": "噫",
                                "datum": 1
                            },
                            {
                                "id": "黟",
                                "datum": 1
                            },
                            {
                                "id": "洢",
                                "datum": 1
                            },
                            {
                                "id": "繄",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "yǐ",
                        "datum": 1,
                        "children": [
                            {
                                "id": "乙",
                                "datum": 1
                            },
                            {
                                "id": "已",
                                "datum": 1
                            },
                            {
                                "id": "以",
                                "datum": 1
                            },
                            {
                                "id": "尾",
                                "datum": 1
                            },
                            {
                                "id": "矣",
                                "datum": 1
                            },
                            {
                                "id": "蚁",
                                "datum": 1
                            },
                            {
                                "id": "倚",
                                "datum": 1
                            },
                            {
                                "id": "椅",
                                "datum": 1
                            },
                            {
                                "id": "钇",
                                "datum": 1
                            },
                            {
                                "id": "苡",
                                "datum": 1
                            },
                            {
                                "id": "迤",
                                "datum": 1
                            },
                            {
                                "id": "旖",
                                "datum": 1
                            },
                            {
                                "id": "佁",
                                "datum": 1
                            },
                            {
                                "id": "舣",
                                "datum": 1
                            },
                            {
                                "id": "酏",
                                "datum": 1
                            },
                            {
                                "id": "扆",
                                "datum": 1
                            },
                            {
                                "id": "𫖮",
                                "datum": 1
                            },
                            {
                                "id": "踦",
                                "datum": 1
                            },
                            {
                                "id": "𬺈",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "yì",
                        "datum": 1,
                        "children": [
                            {
                                "id": "亿",
                                "datum": 1
                            },
                            {
                                "id": "义",
                                "datum": 1
                            },
                            {
                                "id": "艺",
                                "datum": 1
                            },
                            {
                                "id": "忆",
                                "datum": 1
                            },
                            {
                                "id": "艾",
                                "datum": 1
                            },
                            {
                                "id": "议",
                                "datum": 1
                            },
                            {
                                "id": "屹",
                                "datum": 1
                            },
                            {
                                "id": "亦",
                                "datum": 1
                            },
                            {
                                "id": "异",
                                "datum": 1
                            },
                            {
                                "id": "抑",
                                "datum": 1
                            },
                            {
                                "id": "邑",
                                "datum": 1
                            },
                            {
                                "id": "役",
                                "datum": 1
                            },
                            {
                                "id": "译",
                                "datum": 1
                            },
                            {
                                "id": "易",
                                "datum": 1
                            },
                            {
                                "id": "绎",
                                "datum": 1
                            },
                            {
                                "id": "疫",
                                "datum": 1
                            },
                            {
                                "id": "益",
                                "datum": 1
                            },
                            {
                                "id": "谊",
                                "datum": 1
                            },
                            {
                                "id": "逸",
                                "datum": 1
                            },
                            {
                                "id": "意",
                                "datum": 1
                            },
                            {
                                "id": "溢",
                                "datum": 1
                            },
                            {
                                "id": "毅",
                                "datum": 1
                            },
                            {
                                "id": "翼",
                                "datum": 1
                            },
                            {
                                "id": "乂",
                                "datum": 1
                            },
                            {
                                "id": "弋",
                                "datum": 1
                            },
                            {
                                "id": "刈",
                                "datum": 1
                            },
                            {
                                "id": "呓",
                                "datum": 1
                            },
                            {
                                "id": "佚",
                                "datum": 1
                            },
                            {
                                "id": "峄",
                                "datum": 1
                            },
                            {
                                "id": "佾",
                                "datum": 1
                            },
                            {
                                "id": "怿",
                                "datum": 1
                            },
                            {
                                "id": "诣",
                                "datum": 1
                            },
                            {
                                "id": "驿",
                                "datum": 1
                            },
                            {
                                "id": "轶",
                                "datum": 1
                            },
                            {
                                "id": "弈",
                                "datum": 1
                            },
                            {
                                "id": "奕",
                                "datum": 1
                            },
                            {
                                "id": "羿",
                                "datum": 1
                            },
                            {
                                "id": "挹",
                                "datum": 1
                            },
                            {
                                "id": "浥",
                                "datum": 1
                            },
                            {
                                "id": "悒",
                                "datum": 1
                            },
                            {
                                "id": "埸",
                                "datum": 1
                            },
                            {
                                "id": "翊",
                                "datum": 1
                            },
                            {
                                "id": "翌",
                                "datum": 1
                            },
                            {
                                "id": "嗌",
                                "datum": 1
                            },
                            {
                                "id": "肄",
                                "datum": 1
                            },
                            {
                                "id": "裔",
                                "datum": 1
                            },
                            {
                                "id": "缢",
                                "datum": 1
                            },
                            {
                                "id": "蜴",
                                "datum": 1
                            },
                            {
                                "id": "镒",
                                "datum": 1
                            },
                            {
                                "id": "熠",
                                "datum": 1
                            },
                            {
                                "id": "薏",
                                "datum": 1
                            },
                            {
                                "id": "殪",
                                "datum": 1
                            },
                            {
                                "id": "螠",
                                "datum": 1
                            },
                            {
                                "id": "劓",
                                "datum": 1
                            },
                            {
                                "id": "翳",
                                "datum": 1
                            },
                            {
                                "id": "臆",
                                "datum": 1
                            },
                            {
                                "id": "癔",
                                "datum": 1
                            },
                            {
                                "id": "懿",
                                "datum": 1
                            },
                            {
                                "id": "杙",
                                "datum": 1
                            },
                            {
                                "id": "枍",
                                "datum": 1
                            },
                            {
                                "id": "𬬩",
                                "datum": 1
                            },
                            {
                                "id": "㑊",
                                "datum": 1
                            },
                            {
                                "id": "勚",
                                "datum": 1
                            },
                            {
                                "id": "裛",
                                "datum": 1
                            },
                            {
                                "id": "廙",
                                "datum": 1
                            },
                            {
                                "id": "瘗",
                                "datum": 1
                            },
                            {
                                "id": "潩",
                                "datum": 1
                            },
                            {
                                "id": "嫕",
                                "datum": 1
                            },
                            {
                                "id": "鹝",
                                "datum": 1
                            },
                            {
                                "id": "鹢",
                                "datum": 1
                            },
                            {
                                "id": "燚",
                                "datum": 1
                            },
                            {
                                "id": "𫄷",
                                "datum": 1
                            },
                            {
                                "id": "𬟁",
                                "datum": 1
                            },
                            {
                                "id": "镱",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "yí",
                        "datum": 1,
                        "children": [
                            {
                                "id": "仪",
                                "datum": 1
                            },
                            {
                                "id": "夷",
                                "datum": 1
                            },
                            {
                                "id": "怡",
                                "datum": 1
                            },
                            {
                                "id": "宜",
                                "datum": 1
                            },
                            {
                                "id": "贻",
                                "datum": 1
                            },
                            {
                                "id": "姨",
                                "datum": 1
                            },
                            {
                                "id": "胰",
                                "datum": 1
                            },
                            {
                                "id": "移",
                                "datum": 1
                            },
                            {
                                "id": "遗",
                                "datum": 1
                            },
                            {
                                "id": "疑",
                                "datum": 1
                            },
                            {
                                "id": "匜",
                                "datum": 1
                            },
                            {
                                "id": "圯",
                                "datum": 1
                            },
                            {
                                "id": "沂",
                                "datum": 1
                            },
                            {
                                "id": "诒",
                                "datum": 1
                            },
                            {
                                "id": "迤",
                                "datum": 1
                            },
                            {
                                "id": "饴",
                                "datum": 1
                            },
                            {
                                "id": "荑",
                                "datum": 1
                            },
                            {
                                "id": "咦",
                                "datum": 1
                            },
                            {
                                "id": "眙",
                                "datum": 1
                            },
                            {
                                "id": "痍",
                                "datum": 1
                            },
                            {
                                "id": "颐",
                                "datum": 1
                            },
                            {
                                "id": "嶷",
                                "datum": 1
                            },
                            {
                                "id": "彝",
                                "datum": 1
                            },
                            {
                                "id": "宧",
                                "datum": 1
                            },
                            {
                                "id": "扅",
                                "datum": 1
                            },
                            {
                                "id": "椸",
                                "datum": 1
                            },
                            {
                                "id": "簃",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "er",
                "datum": 1,
                "children": [
                    {
                        "id": "èr",
                        "datum": 1,
                        "children": [
                            {
                                "id": "二",
                                "datum": 1
                            },
                            {
                                "id": "贰",
                                "datum": 1
                            },
                            {
                                "id": "咡",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "ér",
                        "datum": 1,
                        "children": [
                            {
                                "id": "儿",
                                "datum": 1
                            },
                            {
                                "id": "而",
                                "datum": 1
                            },
                            {
                                "id": "鸸",
                                "datum": 1
                            },
                            {
                                "id": "陑",
                                "datum": 1
                            },
                            {
                                "id": "耏",
                                "datum": 1
                            },
                            {
                                "id": "鲕",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "ěr",
                        "datum": 1,
                        "children": [
                            {
                                "id": "尔",
                                "datum": 1
                            },
                            {
                                "id": "耳",
                                "datum": 1
                            },
                            {
                                "id": "饵",
                                "datum": 1
                            },
                            {
                                "id": "迩",
                                "datum": 1
                            },
                            {
                                "id": "洱",
                                "datum": 1
                            },
                            {
                                "id": "珥",
                                "datum": 1
                            },
                            {
                                "id": "铒",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "shi",
                "datum": 1,
                "children": [
                    {
                        "id": "shí",
                        "datum": 1,
                        "children": [
                            {
                                "id": "十",
                                "datum": 1
                            },
                            {
                                "id": "什",
                                "datum": 1
                            },
                            {
                                "id": "石",
                                "datum": 1
                            },
                            {
                                "id": "时",
                                "datum": 1
                            },
                            {
                                "id": "识",
                                "datum": 1
                            },
                            {
                                "id": "实",
                                "datum": 1
                            },
                            {
                                "id": "拾",
                                "datum": 1
                            },
                            {
                                "id": "食",
                                "datum": 1
                            },
                            {
                                "id": "蚀",
                                "datum": 1
                            },
                            {
                                "id": "炻",
                                "datum": 1
                            },
                            {
                                "id": "埘",
                                "datum": 1
                            },
                            {
                                "id": "莳",
                                "datum": 1
                            },
                            {
                                "id": "湜",
                                "datum": 1
                            },
                            {
                                "id": "鲥",
                                "datum": 1
                            },
                            {
                                "id": "祏",
                                "datum": 1
                            },
                            {
                                "id": "鼫",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "shì",
                        "datum": 1,
                        "children": [
                            {
                                "id": "士",
                                "datum": 1
                            },
                            {
                                "id": "氏",
                                "datum": 1
                            },
                            {
                                "id": "示",
                                "datum": 1
                            },
                            {
                                "id": "世",
                                "datum": 1
                            },
                            {
                                "id": "市",
                                "datum": 1
                            },
                            {
                                "id": "式",
                                "datum": 1
                            },
                            {
                                "id": "似",
                                "datum": 1
                            },
                            {
                                "id": "势",
                                "datum": 1
                            },
                            {
                                "id": "事",
                                "datum": 1
                            },
                            {
                                "id": "侍",
                                "datum": 1
                            },
                            {
                                "id": "饰",
                                "datum": 1
                            },
                            {
                                "id": "试",
                                "datum": 1
                            },
                            {
                                "id": "视",
                                "datum": 1
                            },
                            {
                                "id": "拭",
                                "datum": 1
                            },
                            {
                                "id": "柿",
                                "datum": 1
                            },
                            {
                                "id": "是",
                                "datum": 1
                            },
                            {
                                "id": "适",
                                "datum": 1
                            },
                            {
                                "id": "恃",
                                "datum": 1
                            },
                            {
                                "id": "室",
                                "datum": 1
                            },
                            {
                                "id": "逝",
                                "datum": 1
                            },
                            {
                                "id": "释",
                                "datum": 1
                            },
                            {
                                "id": "嗜",
                                "datum": 1
                            },
                            {
                                "id": "誓",
                                "datum": 1
                            },
                            {
                                "id": "仕",
                                "datum": 1
                            },
                            {
                                "id": "贳",
                                "datum": 1
                            },
                            {
                                "id": "峙",
                                "datum": 1
                            },
                            {
                                "id": "莳",
                                "datum": 1
                            },
                            {
                                "id": "轼",
                                "datum": 1
                            },
                            {
                                "id": "铈",
                                "datum": 1
                            },
                            {
                                "id": "舐",
                                "datum": 1
                            },
                            {
                                "id": "弑",
                                "datum": 1
                            },
                            {
                                "id": "谥",
                                "datum": 1
                            },
                            {
                                "id": "筮",
                                "datum": 1
                            },
                            {
                                "id": "奭",
                                "datum": 1
                            },
                            {
                                "id": "噬",
                                "datum": 1
                            },
                            {
                                "id": "螫",
                                "datum": 1
                            },
                            {
                                "id": "䏡",
                                "datum": 1
                            },
                            {
                                "id": "栻",
                                "datum": 1
                            },
                            {
                                "id": "𬤊",
                                "datum": 1
                            },
                            {
                                "id": "媞",
                                "datum": 1
                            },
                            {
                                "id": "襫",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "shī",
                        "datum": 1,
                        "children": [
                            {
                                "id": "尸",
                                "datum": 1
                            },
                            {
                                "id": "失",
                                "datum": 1
                            },
                            {
                                "id": "师",
                                "datum": 1
                            },
                            {
                                "id": "诗",
                                "datum": 1
                            },
                            {
                                "id": "狮",
                                "datum": 1
                            },
                            {
                                "id": "施",
                                "datum": 1
                            },
                            {
                                "id": "湿",
                                "datum": 1
                            },
                            {
                                "id": "虱",
                                "datum": 1
                            },
                            {
                                "id": "蓍",
                                "datum": 1
                            },
                            {
                                "id": "嘘",
                                "datum": 1
                            },
                            {
                                "id": "邿",
                                "datum": 1
                            },
                            {
                                "id": "鸤",
                                "datum": 1
                            },
                            {
                                "id": "䴓",
                                "datum": 1
                            },
                            {
                                "id": "浉",
                                "datum": 1
                            },
                            {
                                "id": "酾",
                                "datum": 1
                            },
                            {
                                "id": "𫚕",
                                "datum": 1
                            },
                            {
                                "id": "鲺",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "shǐ",
                        "datum": 1,
                        "children": [
                            {
                                "id": "史",
                                "datum": 1
                            },
                            {
                                "id": "矢",
                                "datum": 1
                            },
                            {
                                "id": "使",
                                "datum": 1
                            },
                            {
                                "id": "始",
                                "datum": 1
                            },
                            {
                                "id": "驶",
                                "datum": 1
                            },
                            {
                                "id": "屎",
                                "datum": 1
                            },
                            {
                                "id": "豕",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "shi",
                        "datum": 1,
                        "children": [
                            {
                                "id": "匙",
                                "datum": 1
                            },
                            {
                                "id": "殖",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "ding",
                "datum": 1,
                "children": [
                    {
                        "id": "dīng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "丁",
                                "datum": 1
                            },
                            {
                                "id": "叮",
                                "datum": 1
                            },
                            {
                                "id": "盯",
                                "datum": 1
                            },
                            {
                                "id": "钉",
                                "datum": 1
                            },
                            {
                                "id": "仃",
                                "datum": 1
                            },
                            {
                                "id": "玎",
                                "datum": 1
                            },
                            {
                                "id": "町",
                                "datum": 1
                            },
                            {
                                "id": "疔",
                                "datum": 1
                            },
                            {
                                "id": "酊",
                                "datum": 1
                            },
                            {
                                "id": "耵",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "dìng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "订",
                                "datum": 1
                            },
                            {
                                "id": "钉",
                                "datum": 1
                            },
                            {
                                "id": "定",
                                "datum": 1
                            },
                            {
                                "id": "啶",
                                "datum": 1
                            },
                            {
                                "id": "腚",
                                "datum": 1
                            },
                            {
                                "id": "碇",
                                "datum": 1
                            },
                            {
                                "id": "锭",
                                "datum": 1
                            },
                            {
                                "id": "萣",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "dǐng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "顶",
                                "datum": 1
                            },
                            {
                                "id": "鼎",
                                "datum": 1
                            },
                            {
                                "id": "酊",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "chang",
                "datum": 1,
                "children": [
                    {
                        "id": "chǎng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "厂",
                                "datum": 1
                            },
                            {
                                "id": "场",
                                "datum": 1
                            },
                            {
                                "id": "敞",
                                "datum": 1
                            },
                            {
                                "id": "昶",
                                "datum": 1
                            },
                            {
                                "id": "惝",
                                "datum": 1
                            },
                            {
                                "id": "氅",
                                "datum": 1
                            },
                            {
                                "id": "𬬮",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "cháng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "长",
                                "datum": 1
                            },
                            {
                                "id": "场",
                                "datum": 1
                            },
                            {
                                "id": "肠",
                                "datum": 1
                            },
                            {
                                "id": "尝",
                                "datum": 1
                            },
                            {
                                "id": "常",
                                "datum": 1
                            },
                            {
                                "id": "偿",
                                "datum": 1
                            },
                            {
                                "id": "苌",
                                "datum": 1
                            },
                            {
                                "id": "徜",
                                "datum": 1
                            },
                            {
                                "id": "嫦",
                                "datum": 1
                            },
                            {
                                "id": "鲿",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "chāng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "昌",
                                "datum": 1
                            },
                            {
                                "id": "猖",
                                "datum": 1
                            },
                            {
                                "id": "伥",
                                "datum": 1
                            },
                            {
                                "id": "菖",
                                "datum": 1
                            },
                            {
                                "id": "阊",
                                "datum": 1
                            },
                            {
                                "id": "娼",
                                "datum": 1
                            },
                            {
                                "id": "鲳",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "chàng",
                        "datum": 1,
                        "children": [
                            {
                                "id": "畅",
                                "datum": 1
                            },
                            {
                                "id": "倡",
                                "datum": 1
                            },
                            {
                                "id": "唱",
                                "datum": 1
                            },
                            {
                                "id": "怅",
                                "datum": 1
                            },
                            {
                                "id": "鬯",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "qi",
                "datum": 1,
                "children": [
                    {
                        "id": "qī",
                        "datum": 1,
                        "children": [
                            {
                                "id": "七",
                                "datum": 1
                            },
                            {
                                "id": "妻",
                                "datum": 1
                            },
                            {
                                "id": "柒",
                                "datum": 1
                            },
                            {
                                "id": "栖",
                                "datum": 1
                            },
                            {
                                "id": "凄",
                                "datum": 1
                            },
                            {
                                "id": "戚",
                                "datum": 1
                            },
                            {
                                "id": "期",
                                "datum": 1
                            },
                            {
                                "id": "欺",
                                "datum": 1
                            },
                            {
                                "id": "缉",
                                "datum": 1
                            },
                            {
                                "id": "漆",
                                "datum": 1
                            },
                            {
                                "id": "沏",
                                "datum": 1
                            },
                            {
                                "id": "桤",
                                "datum": 1
                            },
                            {
                                "id": "萋",
                                "datum": 1
                            },
                            {
                                "id": "嘁",
                                "datum": 1
                            },
                            {
                                "id": "蹊",
                                "datum": 1
                            },
                            {
                                "id": "郪",
                                "datum": 1
                            },
                            {
                                "id": "欹",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "qǐ",
                        "datum": 1,
                        "children": [
                            {
                                "id": "乞",
                                "datum": 1
                            },
                            {
                                "id": "岂",
                                "datum": 1
                            },
                            {
                                "id": "企",
                                "datum": 1
                            },
                            {
                                "id": "启",
                                "datum": 1
                            },
                            {
                                "id": "起",
                                "datum": 1
                            },
                            {
                                "id": "芑",
                                "datum": 1
                            },
                            {
                                "id": "屺",
                                "datum": 1
                            },
                            {
                                "id": "杞",
                                "datum": 1
                            },
                            {
                                "id": "绮",
                                "datum": 1
                            },
                            {
                                "id": "玘",
                                "datum": 1
                            },
                            {
                                "id": "婍",
                                "datum": 1
                            },
                            {
                                "id": "棨",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "qì",
                        "datum": 1,
                        "children": [
                            {
                                "id": "气",
                                "datum": 1
                            },
                            {
                                "id": "迄",
                                "datum": 1
                            },
                            {
                                "id": "弃",
                                "datum": 1
                            },
                            {
                                "id": "汽",
                                "datum": 1
                            },
                            {
                                "id": "泣",
                                "datum": 1
                            },
                            {
                                "id": "契",
                                "datum": 1
                            },
                            {
                                "id": "砌",
                                "datum": 1
                            },
                            {
                                "id": "器",
                                "datum": 1
                            },
                            {
                                "id": "讫",
                                "datum": 1
                            },
                            {
                                "id": "汔",
                                "datum": 1
                            },
                            {
                                "id": "亟",
                                "datum": 1
                            },
                            {
                                "id": "葺",
                                "datum": 1
                            },
                            {
                                "id": "碛",
                                "datum": 1
                            },
                            {
                                "id": "槭",
                                "datum": 1
                            },
                            {
                                "id": "憩",
                                "datum": 1
                            },
                            {
                                "id": "洓",
                                "datum": 1
                            },
                            {
                                "id": "碶",
                                "datum": 1
                            },
                            {
                                "id": "磜",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "qí",
                        "datum": 1,
                        "children": [
                            {
                                "id": "齐",
                                "datum": 1
                            },
                            {
                                "id": "其",
                                "datum": 1
                            },
                            {
                                "id": "奇",
                                "datum": 1
                            },
                            {
                                "id": "歧",
                                "datum": 1
                            },
                            {
                                "id": "祈",
                                "datum": 1
                            },
                            {
                                "id": "脐",
                                "datum": 1
                            },
                            {
                                "id": "崎",
                                "datum": 1
                            },
                            {
                                "id": "骑",
                                "datum": 1
                            },
                            {
                                "id": "棋",
                                "datum": 1
                            },
                            {
                                "id": "旗",
                                "datum": 1
                            },
                            {
                                "id": "鳍",
                                "datum": 1
                            },
                            {
                                "id": "亓",
                                "datum": 1
                            },
                            {
                                "id": "祁",
                                "datum": 1
                            },
                            {
                                "id": "圻",
                                "datum": 1
                            },
                            {
                                "id": "芪",
                                "datum": 1
                            },
                            {
                                "id": "岐",
                                "datum": 1
                            },
                            {
                                "id": "祇",
                                "datum": 1
                            },
                            {
                                "id": "荠",
                                "datum": 1
                            },
                            {
                                "id": "俟",
                                "datum": 1
                            },
                            {
                                "id": "耆",
                                "datum": 1
                            },
                            {
                                "id": "颀",
                                "datum": 1
                            },
                            {
                                "id": "萁",
                                "datum": 1
                            },
                            {
                                "id": "畦",
                                "datum": 1
                            },
                            {
                                "id": "淇",
                                "datum": 1
                            },
                            {
                                "id": "骐",
                                "datum": 1
                            },
                            {
                                "id": "琪",
                                "datum": 1
                            },
                            {
                                "id": "琦",
                                "datum": 1
                            },
                            {
                                "id": "蛴",
                                "datum": 1
                            },
                            {
                                "id": "祺",
                                "datum": 1
                            },
                            {
                                "id": "锜",
                                "datum": 1
                            },
                            {
                                "id": "綦",
                                "datum": 1
                            },
                            {
                                "id": "蜞",
                                "datum": 1
                            },
                            {
                                "id": "蕲",
                                "datum": 1
                            },
                            {
                                "id": "麒",
                                "datum": 1
                            },
                            {
                                "id": "𨙸",
                                "datum": 1
                            },
                            {
                                "id": "𬨂",
                                "datum": 1
                            },
                            {
                                "id": "埼",
                                "datum": 1
                            },
                            {
                                "id": "䓫",
                                "datum": 1
                            },
                            {
                                "id": "跂",
                                "datum": 1
                            },
                            {
                                "id": "愭",
                                "datum": 1
                            },
                            {
                                "id": "鲯",
                                "datum": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": "bo",
                "datum": 1,
                "children": [
                    {
                        "id": "bo",
                        "datum": 1,
                        "children": [
                            {
                                "id": "卜",
                                "datum": 1
                            },
                            {
                                "id": "啵",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "bó",
                        "datum": 1,
                        "children": [
                            {
                                "id": "伯",
                                "datum": 1
                            },
                            {
                                "id": "驳",
                                "datum": 1
                            },
                            {
                                "id": "泊",
                                "datum": 1
                            },
                            {
                                "id": "柏",
                                "datum": 1
                            },
                            {
                                "id": "勃",
                                "datum": 1
                            },
                            {
                                "id": "舶",
                                "datum": 1
                            },
                            {
                                "id": "脖",
                                "datum": 1
                            },
                            {
                                "id": "博",
                                "datum": 1
                            },
                            {
                                "id": "渤",
                                "datum": 1
                            },
                            {
                                "id": "搏",
                                "datum": 1
                            },
                            {
                                "id": "膊",
                                "datum": 1
                            },
                            {
                                "id": "薄",
                                "datum": 1
                            },
                            {
                                "id": "帛",
                                "datum": 1
                            },
                            {
                                "id": "钹",
                                "datum": 1
                            },
                            {
                                "id": "铂",
                                "datum": 1
                            },
                            {
                                "id": "亳",
                                "datum": 1
                            },
                            {
                                "id": "鹁",
                                "datum": 1
                            },
                            {
                                "id": "僰",
                                "datum": 1
                            },
                            {
                                "id": "箔",
                                "datum": 1
                            },
                            {
                                "id": "礴",
                                "datum": 1
                            },
                            {
                                "id": "浡",
                                "datum": 1
                            },
                            {
                                "id": "袯",
                                "datum": 1
                            },
                            {
                                "id": "桲",
                                "datum": 1
                            },
                            {
                                "id": "艴",
                                "datum": 1
                            },
                            {
                                "id": "鲌",
                                "datum": 1
                            },
                            {
                                "id": "踣",
                                "datum": 1
                            },
                            {
                                "id": "镈",
                                "datum": 1
                            },
                            {
                                "id": "馞",
                                "datum": 1
                            },
                            {
                                "id": "欂",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "bō",
                        "datum": 1,
                        "children": [
                            {
                                "id": "拨",
                                "datum": 1
                            },
                            {
                                "id": "波",
                                "datum": 1
                            },
                            {
                                "id": "玻",
                                "datum": 1
                            },
                            {
                                "id": "剥",
                                "datum": 1
                            },
                            {
                                "id": "菠",
                                "datum": 1
                            },
                            {
                                "id": "播",
                                "datum": 1
                            },
                            {
                                "id": "钵",
                                "datum": 1
                            },
                            {
                                "id": "饽",
                                "datum": 1
                            },
                            {
                                "id": "蕃",
                                "datum": 1
                            },
                            {
                                "id": "砵",
                                "datum": 1
                            },
                            {
                                "id": "哱",
                                "datum": 1
                            },
                            {
                                "id": "𬭛",
                                "datum": 1
                            },
                            {
                                "id": "嶓",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "bǒ",
                        "datum": 1,
                        "children": [
                            {
                                "id": "跛",
                                "datum": 1
                            },
                            {
                                "id": "簸",
                                "datum": 1
                            }
                        ]
                    },
                    {
                        "id": "bò",
                        "datum": 1,
                        "children": [
                            {
                                "id": "薄",
                                "datum": 1
                            },
                            {
                                "id": "簸",
                                "datum": 1
                            },
                            {
                                "id": "檗",
                                "datum": 1
                            },
                            {
                                "id": "擘",
                                "datum": 1
                            }
                        ]
                    }
                ]
            }
        ]
    }
]

# Compute circle positions thanks to the circlify() function
circles = circlify.circlify(
    data,
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create just a figure and only one subplot
fig, ax = plt.subplots(figsize=(14, 14))

# Title
ax.set_title('拼音分组汉字图')

# Remove axes
ax.axis('off')

# Find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    # Circles in depth level 1
    if circle.level == 1:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
    # Circles in depth level 2: Pinyin without accents
    if circle.level == 2:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.25))
    # Circles in depth level 3: Pinyin with accents
    if circle.level == 3:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="white", edgecolor="black"))
        # Add label
        label = circle.ex["id"]
        plt.annotate(label, (x, y + r), va='center', ha='center',
                     bbox=dict(
                         facecolor='white',
                         edgecolor='black',
                         boxstyle='round',
                         pad=.25))
    # Circles in depth level 4: Chinese characters
    elif circle.level == 4:
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, facecolor="lightblue"))
        # Show label
        label = circle.ex["id"]
        plt.annotate(label, (x, y), va='center', ha='center', color="black")

plt.savefig(os.path.basename(__file__) + '.png', dpi=300)

