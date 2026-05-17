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
                "children": [
                    {
                        "id": "yī",
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
                        ],
                        "datum": 17
                    },
                    {
                        "id": "yǐ",
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
                        ],
                        "datum": 19
                    },
                    {
                        "id": "yì",
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
                        ],
                        "datum": 74
                    },
                    {
                        "id": "yí",
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
                        ],
                        "datum": 27
                    }
                ],
                "datum": 137
            },
            {
                "id": "er",
                "children": [
                    {
                        "id": "èr",
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
                        ],
                        "datum": 3
                    },
                    {
                        "id": "ér",
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
                        ],
                        "datum": 6
                    },
                    {
                        "id": "ěr",
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
                        ],
                        "datum": 7
                    }
                ],
                "datum": 16
            },
            {
                "id": "shi",
                "children": [
                    {
                        "id": "shí",
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
                        ],
                        "datum": 16
                    },
                    {
                        "id": "shì",
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
                        ],
                        "datum": 41
                    },
                    {
                        "id": "shī",
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
                        ],
                        "datum": 17
                    },
                    {
                        "id": "shǐ",
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
                        ],
                        "datum": 7
                    },
                    {
                        "id": "shi",
                        "children": [
                            {
                                "id": "匙",
                                "datum": 1
                            },
                            {
                                "id": "殖",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    }
                ],
                "datum": 83
            },
            {
                "id": "ding",
                "children": [
                    {
                        "id": "dīng",
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
                        ],
                        "datum": 10
                    },
                    {
                        "id": "dìng",
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
                        ],
                        "datum": 8
                    },
                    {
                        "id": "dǐng",
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
                        ],
                        "datum": 3
                    }
                ],
                "datum": 21
            },
            {
                "id": "chang",
                "children": [
                    {
                        "id": "chǎng",
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
                        ],
                        "datum": 7
                    },
                    {
                        "id": "cháng",
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
                        ],
                        "datum": 10
                    },
                    {
                        "id": "chāng",
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
                        ],
                        "datum": 7
                    },
                    {
                        "id": "chàng",
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
                        ],
                        "datum": 5
                    }
                ],
                "datum": 29
            },
            {
                "id": "qi",
                "children": [
                    {
                        "id": "qī",
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
                        ],
                        "datum": 17
                    },
                    {
                        "id": "qǐ",
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
                        ],
                        "datum": 12
                    },
                    {
                        "id": "qì",
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
                        ],
                        "datum": 18
                    },
                    {
                        "id": "qí",
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
                        ],
                        "datum": 41
                    }
                ],
                "datum": 88
            },
            {
                "id": "bo",
                "children": [
                    {
                        "id": "bo",
                        "children": [
                            {
                                "id": "卜",
                                "datum": 1
                            },
                            {
                                "id": "啵",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "bó",
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
                        ],
                        "datum": 29
                    },
                    {
                        "id": "bō",
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
                        ],
                        "datum": 13
                    },
                    {
                        "id": "bǒ",
                        "children": [
                            {
                                "id": "跛",
                                "datum": 1
                            },
                            {
                                "id": "簸",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "bò",
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
                        ],
                        "datum": 4
                    }
                ],
                "datum": 50
            },
            {
                "id": "bu",
                "children": [
                    {
                        "id": "bǔ",
                        "children": [
                            {
                                "id": "卜",
                                "datum": 1
                            },
                            {
                                "id": "补",
                                "datum": 1
                            },
                            {
                                "id": "捕",
                                "datum": 1
                            },
                            {
                                "id": "哺",
                                "datum": 1
                            },
                            {
                                "id": "堡",
                                "datum": 1
                            },
                            {
                                "id": "卟",
                                "datum": 1
                            },
                            {
                                "id": "𬷕",
                                "datum": 1
                            }
                        ],
                        "datum": 7
                    },
                    {
                        "id": "bù",
                        "children": [
                            {
                                "id": "不",
                                "datum": 1
                            },
                            {
                                "id": "布",
                                "datum": 1
                            },
                            {
                                "id": "步",
                                "datum": 1
                            },
                            {
                                "id": "怖",
                                "datum": 1
                            },
                            {
                                "id": "部",
                                "datum": 1
                            },
                            {
                                "id": "埠",
                                "datum": 1
                            },
                            {
                                "id": "簿",
                                "datum": 1
                            },
                            {
                                "id": "钚",
                                "datum": 1
                            },
                            {
                                "id": "埔",
                                "datum": 1
                            },
                            {
                                "id": "瓿",
                                "datum": 1
                            },
                            {
                                "id": "埗",
                                "datum": 1
                            },
                            {
                                "id": "蔀",
                                "datum": 1
                            }
                        ],
                        "datum": 12
                    },
                    {
                        "id": "bū",
                        "children": [
                            {
                                "id": "逋",
                                "datum": 1
                            },
                            {
                                "id": "晡",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "bú",
                        "children": [
                            {
                                "id": "醭",
                                "datum": 1
                            }
                        ],
                        "datum": 1
                    }
                ],
                "datum": 22
            },
            {
                "id": "ba",
                "children": [
                    {
                        "id": "bā",
                        "children": [
                            {
                                "id": "八",
                                "datum": 1
                            },
                            {
                                "id": "巴",
                                "datum": 1
                            },
                            {
                                "id": "扒",
                                "datum": 1
                            },
                            {
                                "id": "叭",
                                "datum": 1
                            },
                            {
                                "id": "芭",
                                "datum": 1
                            },
                            {
                                "id": "吧",
                                "datum": 1
                            },
                            {
                                "id": "疤",
                                "datum": 1
                            },
                            {
                                "id": "捌",
                                "datum": 1
                            },
                            {
                                "id": "笆",
                                "datum": 1
                            },
                            {
                                "id": "粑",
                                "datum": 1
                            },
                            {
                                "id": "朳",
                                "datum": 1
                            },
                            {
                                "id": "岜",
                                "datum": 1
                            },
                            {
                                "id": "蚆",
                                "datum": 1
                            },
                            {
                                "id": "羓",
                                "datum": 1
                            },
                            {
                                "id": "鲃",
                                "datum": 1
                            }
                        ],
                        "datum": 15
                    },
                    {
                        "id": "bà",
                        "children": [
                            {
                                "id": "坝",
                                "datum": 1
                            },
                            {
                                "id": "把",
                                "datum": 1
                            },
                            {
                                "id": "爸",
                                "datum": 1
                            },
                            {
                                "id": "耙",
                                "datum": 1
                            },
                            {
                                "id": "罢",
                                "datum": 1
                            },
                            {
                                "id": "霸",
                                "datum": 1
                            },
                            {
                                "id": "鲅",
                                "datum": 1
                            },
                            {
                                "id": "灞",
                                "datum": 1
                            }
                        ],
                        "datum": 8
                    },
                    {
                        "id": "bǎ",
                        "children": [
                            {
                                "id": "把",
                                "datum": 1
                            },
                            {
                                "id": "靶",
                                "datum": 1
                            },
                            {
                                "id": "钯",
                                "datum": 1
                            }
                        ],
                        "datum": 3
                    },
                    {
                        "id": "ba",
                        "children": [
                            {
                                "id": "吧",
                                "datum": 1
                            },
                            {
                                "id": "罢",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "bá",
                        "children": [
                            {
                                "id": "拔",
                                "datum": 1
                            },
                            {
                                "id": "跋",
                                "datum": 1
                            },
                            {
                                "id": "魃",
                                "datum": 1
                            },
                            {
                                "id": "妭",
                                "datum": 1
                            },
                            {
                                "id": "胈",
                                "datum": 1
                            },
                            {
                                "id": "菝",
                                "datum": 1
                            }
                        ],
                        "datum": 6
                    }
                ],
                "datum": 34
            },
            {
                "id": "ren",
                "children": [
                    {
                        "id": "rén",
                        "children": [
                            {
                                "id": "人",
                                "datum": 1
                            },
                            {
                                "id": "壬",
                                "datum": 1
                            },
                            {
                                "id": "仁",
                                "datum": 1
                            },
                            {
                                "id": "任",
                                "datum": 1
                            }
                        ],
                        "datum": 4
                    },
                    {
                        "id": "rèn",
                        "children": [
                            {
                                "id": "刃",
                                "datum": 1
                            },
                            {
                                "id": "认",
                                "datum": 1
                            },
                            {
                                "id": "任",
                                "datum": 1
                            },
                            {
                                "id": "纫",
                                "datum": 1
                            },
                            {
                                "id": "韧",
                                "datum": 1
                            },
                            {
                                "id": "仞",
                                "datum": 1
                            },
                            {
                                "id": "轫",
                                "datum": 1
                            },
                            {
                                "id": "饪",
                                "datum": 1
                            },
                            {
                                "id": "妊",
                                "datum": 1
                            },
                            {
                                "id": "纴",
                                "datum": 1
                            },
                            {
                                "id": "衽",
                                "datum": 1
                            },
                            {
                                "id": "葚",
                                "datum": 1
                            },
                            {
                                "id": "讱",
                                "datum": 1
                            }
                        ],
                        "datum": 13
                    },
                    {
                        "id": "rěn",
                        "children": [
                            {
                                "id": "忍",
                                "datum": 1
                            },
                            {
                                "id": "荏",
                                "datum": 1
                            },
                            {
                                "id": "稔",
                                "datum": 1
                            }
                        ],
                        "datum": 3
                    }
                ],
                "datum": 20
            },
            {
                "id": "ru",
                "children": [
                    {
                        "id": "rù",
                        "children": [
                            {
                                "id": "入",
                                "datum": 1
                            },
                            {
                                "id": "褥",
                                "datum": 1
                            },
                            {
                                "id": "洳",
                                "datum": 1
                            },
                            {
                                "id": "蓐",
                                "datum": 1
                            },
                            {
                                "id": "溽",
                                "datum": 1
                            },
                            {
                                "id": "缛",
                                "datum": 1
                            }
                        ],
                        "datum": 6
                    },
                    {
                        "id": "rǔ",
                        "children": [
                            {
                                "id": "汝",
                                "datum": 1
                            },
                            {
                                "id": "乳",
                                "datum": 1
                            },
                            {
                                "id": "辱",
                                "datum": 1
                            }
                        ],
                        "datum": 3
                    },
                    {
                        "id": "rú",
                        "children": [
                            {
                                "id": "如",
                                "datum": 1
                            },
                            {
                                "id": "儒",
                                "datum": 1
                            },
                            {
                                "id": "蠕",
                                "datum": 1
                            },
                            {
                                "id": "茹",
                                "datum": 1
                            },
                            {
                                "id": "铷",
                                "datum": 1
                            },
                            {
                                "id": "薷",
                                "datum": 1
                            },
                            {
                                "id": "嚅",
                                "datum": 1
                            },
                            {
                                "id": "濡",
                                "datum": 1
                            },
                            {
                                "id": "孺",
                                "datum": 1
                            },
                            {
                                "id": "襦",
                                "datum": 1
                            },
                            {
                                "id": "嬬",
                                "datum": 1
                            },
                            {
                                "id": "颥",
                                "datum": 1
                            }
                        ],
                        "datum": 12
                    }
                ],
                "datum": 21
            },
            {
                "id": "bi",
                "children": [
                    {
                        "id": "bǐ",
                        "children": [
                            {
                                "id": "匕",
                                "datum": 1
                            },
                            {
                                "id": "比",
                                "datum": 1
                            },
                            {
                                "id": "彼",
                                "datum": 1
                            },
                            {
                                "id": "笔",
                                "datum": 1
                            },
                            {
                                "id": "鄙",
                                "datum": 1
                            },
                            {
                                "id": "吡",
                                "datum": 1
                            },
                            {
                                "id": "妣",
                                "datum": 1
                            },
                            {
                                "id": "秕",
                                "datum": 1
                            },
                            {
                                "id": "俾",
                                "datum": 1
                            },
                            {
                                "id": "芘",
                                "datum": 1
                            },
                            {
                                "id": "沘",
                                "datum": 1
                            },
                            {
                                "id": "舭",
                                "datum": 1
                            }
                        ],
                        "datum": 12
                    },
                    {
                        "id": "bì",
                        "children": [
                            {
                                "id": "币",
                                "datum": 1
                            },
                            {
                                "id": "必",
                                "datum": 1
                            },
                            {
                                "id": "毕",
                                "datum": 1
                            },
                            {
                                "id": "闭",
                                "datum": 1
                            },
                            {
                                "id": "庇",
                                "datum": 1
                            },
                            {
                                "id": "泌",
                                "datum": 1
                            },
                            {
                                "id": "毙",
                                "datum": 1
                            },
                            {
                                "id": "秘",
                                "datum": 1
                            },
                            {
                                "id": "痹",
                                "datum": 1
                            },
                            {
                                "id": "辟",
                                "datum": 1
                            },
                            {
                                "id": "碧",
                                "datum": 1
                            },
                            {
                                "id": "蔽",
                                "datum": 1
                            },
                            {
                                "id": "弊",
                                "datum": 1
                            },
                            {
                                "id": "壁",
                                "datum": 1
                            },
                            {
                                "id": "避",
                                "datum": 1
                            },
                            {
                                "id": "臂",
                                "datum": 1
                            },
                            {
                                "id": "璧",
                                "datum": 1
                            },
                            {
                                "id": "畀",
                                "datum": 1
                            },
                            {
                                "id": "荜",
                                "datum": 1
                            },
                            {
                                "id": "毖",
                                "datum": 1
                            },
                            {
                                "id": "哔",
                                "datum": 1
                            },
                            {
                                "id": "陛",
                                "datum": 1
                            },
                            {
                                "id": "铋",
                                "datum": 1
                            },
                            {
                                "id": "敝",
                                "datum": 1
                            },
                            {
                                "id": "婢",
                                "datum": 1
                            },
                            {
                                "id": "筚",
                                "datum": 1
                            },
                            {
                                "id": "愎",
                                "datum": 1
                            },
                            {
                                "id": "弼",
                                "datum": 1
                            },
                            {
                                "id": "蓖",
                                "datum": 1
                            },
                            {
                                "id": "跸",
                                "datum": 1
                            },
                            {
                                "id": "滗",
                                "datum": 1
                            },
                            {
                                "id": "裨",
                                "datum": 1
                            },
                            {
                                "id": "箅",
                                "datum": 1
                            },
                            {
                                "id": "薜",
                                "datum": 1
                            },
                            {
                                "id": "篦",
                                "datum": 1
                            },
                            {
                                "id": "嬖",
                                "datum": 1
                            },
                            {
                                "id": "髀",
                                "datum": 1
                            },
                            {
                                "id": "濞",
                                "datum": 1
                            },
                            {
                                "id": "襞",
                                "datum": 1
                            },
                            {
                                "id": "坒",
                                "datum": 1
                            },
                            {
                                "id": "佖",
                                "datum": 1
                            },
                            {
                                "id": "邲",
                                "datum": 1
                            },
                            {
                                "id": "诐",
                                "datum": 1
                            },
                            {
                                "id": "苾",
                                "datum": 1
                            },
                            {
                                "id": "咇",
                                "datum": 1
                            },
                            {
                                "id": "珌",
                                "datum": 1
                            },
                            {
                                "id": "狴",
                                "datum": 1
                            },
                            {
                                "id": "萆",
                                "datum": 1
                            },
                            {
                                "id": "庳",
                                "datum": 1
                            },
                            {
                                "id": "皕",
                                "datum": 1
                            },
                            {
                                "id": "赑",
                                "datum": 1
                            },
                            {
                                "id": "馝",
                                "datum": 1
                            },
                            {
                                "id": "觱",
                                "datum": 1
                            }
                        ],
                        "datum": 53
                    },
                    {
                        "id": "bī",
                        "children": [
                            {
                                "id": "逼",
                                "datum": 1
                            },
                            {
                                "id": "鲾",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "bí",
                        "children": [
                            {
                                "id": "鼻",
                                "datum": 1
                            },
                            {
                                "id": "荸",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    }
                ],
                "datum": 69
            },
            {
                "id": "ji",
                "children": [
                    {
                        "id": "jī",
                        "children": [
                            {
                                "id": "几",
                                "datum": 1
                            },
                            {
                                "id": "讥",
                                "datum": 1
                            },
                            {
                                "id": "击",
                                "datum": 1
                            },
                            {
                                "id": "叽",
                                "datum": 1
                            },
                            {
                                "id": "饥",
                                "datum": 1
                            },
                            {
                                "id": "圾",
                                "datum": 1
                            },
                            {
                                "id": "机",
                                "datum": 1
                            },
                            {
                                "id": "肌",
                                "datum": 1
                            },
                            {
                                "id": "鸡",
                                "datum": 1
                            },
                            {
                                "id": "奇",
                                "datum": 1
                            },
                            {
                                "id": "唧",
                                "datum": 1
                            },
                            {
                                "id": "积",
                                "datum": 1
                            },
                            {
                                "id": "基",
                                "datum": 1
                            },
                            {
                                "id": "期",
                                "datum": 1
                            },
                            {
                                "id": "缉",
                                "datum": 1
                            },
                            {
                                "id": "畸",
                                "datum": 1
                            },
                            {
                                "id": "箕",
                                "datum": 1
                            },
                            {
                                "id": "稽",
                                "datum": 1
                            },
                            {
                                "id": "激",
                                "datum": 1
                            },
                            {
                                "id": "玑",
                                "datum": 1
                            },
                            {
                                "id": "芨",
                                "datum": 1
                            },
                            {
                                "id": "乩",
                                "datum": 1
                            },
                            {
                                "id": "矶",
                                "datum": 1
                            },
                            {
                                "id": "剞",
                                "datum": 1
                            },
                            {
                                "id": "笄",
                                "datum": 1
                            },
                            {
                                "id": "屐",
                                "datum": 1
                            },
                            {
                                "id": "姬",
                                "datum": 1
                            },
                            {
                                "id": "赍",
                                "datum": 1
                            },
                            {
                                "id": "犄",
                                "datum": 1
                            },
                            {
                                "id": "嵇",
                                "datum": 1
                            },
                            {
                                "id": "跻",
                                "datum": 1
                            },
                            {
                                "id": "齑",
                                "datum": 1
                            },
                            {
                                "id": "畿",
                                "datum": 1
                            },
                            {
                                "id": "墼",
                                "datum": 1
                            },
                            {
                                "id": "羁",
                                "datum": 1
                            },
                            {
                                "id": "枅",
                                "datum": 1
                            },
                            {
                                "id": "𬯀",
                                "datum": 1
                            },
                            {
                                "id": "𫓯",
                                "datum": 1
                            },
                            {
                                "id": "𫓹",
                                "datum": 1
                            },
                            {
                                "id": "𫌀",
                                "datum": 1
                            },
                            {
                                "id": "觭",
                                "datum": 1
                            }
                        ],
                        "datum": 41
                    },
                    {
                        "id": "jǐ",
                        "children": [
                            {
                                "id": "几",
                                "datum": 1
                            },
                            {
                                "id": "己",
                                "datum": 1
                            },
                            {
                                "id": "纪",
                                "datum": 1
                            },
                            {
                                "id": "挤",
                                "datum": 1
                            },
                            {
                                "id": "济",
                                "datum": 1
                            },
                            {
                                "id": "给",
                                "datum": 1
                            },
                            {
                                "id": "脊",
                                "datum": 1
                            },
                            {
                                "id": "虮",
                                "datum": 1
                            },
                            {
                                "id": "戟",
                                "datum": 1
                            },
                            {
                                "id": "麂",
                                "datum": 1
                            },
                            {
                                "id": "掎",
                                "datum": 1
                            },
                            {
                                "id": "鱾",
                                "datum": 1
                            }
                        ],
                        "datum": 12
                    },
                    {
                        "id": "jí",
                        "children": [
                            {
                                "id": "及",
                                "datum": 1
                            },
                            {
                                "id": "吉",
                                "datum": 1
                            },
                            {
                                "id": "级",
                                "datum": 1
                            },
                            {
                                "id": "极",
                                "datum": 1
                            },
                            {
                                "id": "即",
                                "datum": 1
                            },
                            {
                                "id": "急",
                                "datum": 1
                            },
                            {
                                "id": "疾",
                                "datum": 1
                            },
                            {
                                "id": "棘",
                                "datum": 1
                            },
                            {
                                "id": "集",
                                "datum": 1
                            },
                            {
                                "id": "辑",
                                "datum": 1
                            },
                            {
                                "id": "嫉",
                                "datum": 1
                            },
                            {
                                "id": "藉",
                                "datum": 1
                            },
                            {
                                "id": "籍",
                                "datum": 1
                            },
                            {
                                "id": "岌",
                                "datum": 1
                            },
                            {
                                "id": "汲",
                                "datum": 1
                            },
                            {
                                "id": "佶",
                                "datum": 1
                            },
                            {
                                "id": "亟",
                                "datum": 1
                            },
                            {
                                "id": "笈",
                                "datum": 1
                            },
                            {
                                "id": "殛",
                                "datum": 1
                            },
                            {
                                "id": "戢",
                                "datum": 1
                            },
                            {
                                "id": "蒺",
                                "datum": 1
                            },
                            {
                                "id": "楫",
                                "datum": 1
                            },
                            {
                                "id": "嵴",
                                "datum": 1
                            },
                            {
                                "id": "蕺",
                                "datum": 1
                            },
                            {
                                "id": "瘠",
                                "datum": 1
                            },
                            {
                                "id": "伋",
                                "datum": 1
                            },
                            {
                                "id": "姞",
                                "datum": 1
                            },
                            {
                                "id": "堲",
                                "datum": 1
                            },
                            {
                                "id": "㴔",
                                "datum": 1
                            },
                            {
                                "id": "耤",
                                "datum": 1
                            },
                            {
                                "id": "鹡",
                                "datum": 1
                            },
                            {
                                "id": "蹐",
                                "datum": 1
                            }
                        ],
                        "datum": 32
                    },
                    {
                        "id": "jì",
                        "children": [
                            {
                                "id": "计",
                                "datum": 1
                            },
                            {
                                "id": "记",
                                "datum": 1
                            },
                            {
                                "id": "纪",
                                "datum": 1
                            },
                            {
                                "id": "技",
                                "datum": 1
                            },
                            {
                                "id": "系",
                                "datum": 1
                            },
                            {
                                "id": "忌",
                                "datum": 1
                            },
                            {
                                "id": "际",
                                "datum": 1
                            },
                            {
                                "id": "妓",
                                "datum": 1
                            },
                            {
                                "id": "季",
                                "datum": 1
                            },
                            {
                                "id": "剂",
                                "datum": 1
                            },
                            {
                                "id": "迹",
                                "datum": 1
                            },
                            {
                                "id": "济",
                                "datum": 1
                            },
                            {
                                "id": "既",
                                "datum": 1
                            },
                            {
                                "id": "继",
                                "datum": 1
                            },
                            {
                                "id": "祭",
                                "datum": 1
                            },
                            {
                                "id": "寄",
                                "datum": 1
                            },
                            {
                                "id": "寂",
                                "datum": 1
                            },
                            {
                                "id": "绩",
                                "datum": 1
                            },
                            {
                                "id": "鲫",
                                "datum": 1
                            },
                            {
                                "id": "冀",
                                "datum": 1
                            },
                            {
                                "id": "伎",
                                "datum": 1
                            },
                            {
                                "id": "荠",
                                "datum": 1
                            },
                            {
                                "id": "洎",
                                "datum": 1
                            },
                            {
                                "id": "觊",
                                "datum": 1
                            },
                            {
                                "id": "偈",
                                "datum": 1
                            },
                            {
                                "id": "悸",
                                "datum": 1
                            },
                            {
                                "id": "蓟",
                                "datum": 1
                            },
                            {
                                "id": "霁",
                                "datum": 1
                            },
                            {
                                "id": "鲚",
                                "datum": 1
                            },
                            {
                                "id": "暨",
                                "datum": 1
                            },
                            {
                                "id": "稷",
                                "datum": 1
                            },
                            {
                                "id": "髻",
                                "datum": 1
                            },
                            {
                                "id": "罽",
                                "datum": 1
                            },
                            {
                                "id": "骥",
                                "datum": 1
                            },
                            {
                                "id": "芰",
                                "datum": 1
                            },
                            {
                                "id": "垍",
                                "datum": 1
                            },
                            {
                                "id": "𪟝",
                                "datum": 1
                            },
                            {
                                "id": "徛",
                                "datum": 1
                            },
                            {
                                "id": "惎",
                                "datum": 1
                            },
                            {
                                "id": "跽",
                                "datum": 1
                            },
                            {
                                "id": "漈",
                                "datum": 1
                            },
                            {
                                "id": "穄",
                                "datum": 1
                            },
                            {
                                "id": "𬶨",
                                "datum": 1
                            },
                            {
                                "id": "𬶭",
                                "datum": 1
                            },
                            {
                                "id": "瀱",
                                "datum": 1
                            }
                        ],
                        "datum": 45
                    }
                ],
                "datum": 130
            },
            {
                "id": "jiu",
                "children": [
                    {
                        "id": "jiǔ",
                        "children": [
                            {
                                "id": "九",
                                "datum": 1
                            },
                            {
                                "id": "久",
                                "datum": 1
                            },
                            {
                                "id": "玖",
                                "datum": 1
                            },
                            {
                                "id": "灸",
                                "datum": 1
                            },
                            {
                                "id": "韭",
                                "datum": 1
                            },
                            {
                                "id": "酒",
                                "datum": 1
                            },
                            {
                                "id": "氿",
                                "datum": 1
                            }
                        ],
                        "datum": 7
                    },
                    {
                        "id": "jiù",
                        "children": [
                            {
                                "id": "旧",
                                "datum": 1
                            },
                            {
                                "id": "臼",
                                "datum": 1
                            },
                            {
                                "id": "疚",
                                "datum": 1
                            },
                            {
                                "id": "救",
                                "datum": 1
                            },
                            {
                                "id": "就",
                                "datum": 1
                            },
                            {
                                "id": "舅",
                                "datum": 1
                            },
                            {
                                "id": "咎",
                                "datum": 1
                            },
                            {
                                "id": "柩",
                                "datum": 1
                            },
                            {
                                "id": "桕",
                                "datum": 1
                            },
                            {
                                "id": "厩",
                                "datum": 1
                            },
                            {
                                "id": "鹫",
                                "datum": 1
                            },
                            {
                                "id": "僦",
                                "datum": 1
                            },
                            {
                                "id": "㠇",
                                "datum": 1
                            }
                        ],
                        "datum": 13
                    },
                    {
                        "id": "jiū",
                        "children": [
                            {
                                "id": "纠",
                                "datum": 1
                            },
                            {
                                "id": "究",
                                "datum": 1
                            },
                            {
                                "id": "揪",
                                "datum": 1
                            },
                            {
                                "id": "鸠",
                                "datum": 1
                            },
                            {
                                "id": "赳",
                                "datum": 1
                            },
                            {
                                "id": "阄",
                                "datum": 1
                            },
                            {
                                "id": "啾",
                                "datum": 1
                            },
                            {
                                "id": "鬏",
                                "datum": 1
                            }
                        ],
                        "datum": 8
                    }
                ],
                "datum": 28
            },
            {
                "id": "diao",
                "children": [
                    {
                        "id": "diāo",
                        "children": [
                            {
                                "id": "刁",
                                "datum": 1
                            },
                            {
                                "id": "叼",
                                "datum": 1
                            },
                            {
                                "id": "雕",
                                "datum": 1
                            },
                            {
                                "id": "凋",
                                "datum": 1
                            },
                            {
                                "id": "貂",
                                "datum": 1
                            },
                            {
                                "id": "碉",
                                "datum": 1
                            },
                            {
                                "id": "鲷",
                                "datum": 1
                            },
                            {
                                "id": "汈",
                                "datum": 1
                            }
                        ],
                        "datum": 8
                    },
                    {
                        "id": "diào",
                        "children": [
                            {
                                "id": "吊",
                                "datum": 1
                            },
                            {
                                "id": "钓",
                                "datum": 1
                            },
                            {
                                "id": "调",
                                "datum": 1
                            },
                            {
                                "id": "掉",
                                "datum": 1
                            },
                            {
                                "id": "铫",
                                "datum": 1
                            },
                            {
                                "id": "窎",
                                "datum": 1
                            },
                            {
                                "id": "铞",
                                "datum": 1
                            }
                        ],
                        "datum": 7
                    }
                ],
                "datum": 15
            },
            {
                "id": "le",
                "children": [
                    {
                        "id": "le",
                        "children": [
                            {
                                "id": "了",
                                "datum": 1
                            },
                            {
                                "id": "饹",
                                "datum": 1
                            }
                        ],
                        "datum": 2
                    },
                    {
                        "id": "lè",
                        "children": [
                            {
                                "id": "乐",
                                "datum": 1
                            },
                            {
                                "id": "勒",
                                "datum": 1
                            },
                            {
                                "id": "仂",
                                "datum": 1
                            },
                            {
                                "id": "叻",
                                "datum": 1
                            },
                            {
                                "id": "泐",
                                "datum": 1
                            },
                            {
                                "id": "鳓",
                                "datum": 1
                            },
                            {
                                "id": "簕",
                                "datum": 1
                            }
                        ],
                        "datum": 7
                    }
                ],
                "datum": 9
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

