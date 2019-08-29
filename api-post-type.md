# Типы открытых публикаций

- [Блог](#blog)
- [Новости](#news)
- [Трейдинг](#trading)
    - [Торговые Сигналы](#trading-signals)
    - [Торговая Стратегия](#trading-startegy)
    - [Торговый Бот](#trading-bot)
- [Образование](#education)

Типы открытых публикаций

| **Post type** | **Child** |
| --- | --- |
| Блог |-|
| **Трейдинг** | Торговые Сигналы |
|| Торговые Стратегии |
|| Торговые Боты |
| Новости |-|
| **Аналитика** | Рыночные Прогнозы |
|| Отчеты по Проектам |
|| Отчеты по Криптовалюте |
| Образование |-|

Таблица access\_type

| **Access type** | **ID** |
| --- | --- |
| Доступно всем | 1 |
| Только для пользователей платформы | 2 |
| Только моим подписчикам | 3 |
| Только для меня | 4 |

Таблица comment\_allow

| **Comment Allow** | **ID** |
| --- | --- |
| Комментирование доступно лишь пользователям платформы | 1 |
| Комментирование доступно только для подписчиков данного пользователя | 2 |
|  Комментирование данного поста ограничено | 3 |

<a name="blog"></a>
## Блог

Формат Ответа

{
    "data": {
        "id": 30286,
        "conversation_id": 18639,
        "post_id": 30286,
        "post_type": "blog",
        "title": "Заголовок публикации",
        "language": {
            "id": 1,
            "native_name": "Русский",
            "code": "ru",
            "flag_icon_url": false
        },
        "pay": 0,
        "cost": 0,
        "user_id": 521,
        "access_type": 1,
        "comment_allow": 2,
        "formatted_created_date": "5 часов назад",
        "formatted_user": {
            "id": 521,
            "first_name": "Ильяс",
            "last_name": "Мейманхан",
            "nickname": "t.estoviiakkaunt.123",
            "account_type": 0,
            "rank_name": "blogger",
            "rank_level": "beginner",
            "value": 0.18,
            "stars": 0,
            "full_name": "Ильяс Мейманхан",
            "full_avatar_url": "https://lh4.googleusercontent.com/-i7M9SefYrKg/AAAAAAAAAAI/AAAAAAAAAAc/nCZxk0V1hLE/photo.jpg",
            "full_avatar_160_url": "https://lh4.googleusercontent.com/-i7M9SefYrKg/AAAAAAAAAAI/AAAAAAAAAAc/nCZxk0V1hLE/photo.jpg",
            "account_type_name": null,
            "account_type_color": null,
            "full_background_url": false
        },
        "statistics": {
            "likes_count": 0,
            "dislikes_count": 0,
            "rating_count": 0,
            "comments_count": 0,
            "purchase_count": 0,
            "repost_count": 0,
            "views": 2,
            "you_liked": false,
            "you_disliked": false,
            "is_favourite": false,
            "you_reposted": false,
            "you_abused": false,
            "visited": true,
            "paid": false,
            "you_pinned": false,
            "archived": false,
            "unique_views": 2
        },
        "subscription_info": {
            "your_post": false,
            "you_followed": false
        },
        "post_type_object": {
            "id": 7,
            "name": "blog",
            "parent_type": null
        },
        "excerpt": "Текст публикации",
        "url_slug": "/blog/30286",
        "url_back_slug": "/blog",
        "tags": [],
        "is_repost": false,
        "has_more_text": false,
        "text": "<p>Текст публикации</p>",св юю
        "postable": {
            "id": 901,
            "category_id": 8,
            "cards": [],
            "category": {
                "id": 8,
                "name": "blogs_categories_life"
            },
            "top_cards": [
                {
                    "value_translation_key": "blogs_categories_life"
                }
            ],
            "full_image_url": "https://dev.taklimakan.network/storage/521/2019/08/19/image/5d5a52994207a.jpg",
            "full_image_250_url": "https://dev.taklimakan.network/storage/521/2019/08/19/image/5d5a52994207a_250.jpg",
            "full_image_800_url": "https://dev.taklimakan.network/storage/521/2019/08/19/image/5d5a52994207a_800.jpg"
        }
    }
}



| Атрибут | Описание |
| --- | --- |
| id  | id публикации |
| conversation\_id | id чата публикации |
| post\_id | id публикации |
| post\_type | тип поста (зависит от сборки) |
| title | Заголовок публикации |
| language.id | id языка публикации |
| language.native\_name | название языка на выбранном языке |
| language.code | краткий код языка |
| language.flag\_icon\_url | ссылка на иконку языка |
| pay | платный/бесплатный контент |
| cost | стоимость контента |
| user\_id | id автора публикации  |
| access\_type | тип доступа, указываемый при создании поста |
| comment\_allow | доступ к комментариям |
| formatted\_created\_date | время создания публикации в человеческом формате |
| formatted\_user.id | id автора публикации |
| formatted\_user.first\_name | имя автора |
| formatted\_user.last\_name | фамилия автора |
| formatted\_user.nickname | никнейм автора |
| formatted\_user.account\_type | тип аккаунта автора |
| formatted\_user.rank\_name | ранг автора, к которому принадлежит публикация |
| formatted\_user.rank\_level | уровень ранга |
| formatted\_user.value | числовой уровень автора по выбранной(к которому принадлежит публикация) сборке |
| formatted\_user.stars | количество звезд автора в выбранном ранге |
| formatted\_user.full\_name | полное имя автора |
| formatted\_user.full\_avatar\_url | ссылка на аватар автора |
| formatted\_user.full\_avatar\_160\_url | ссылка на аватар автора в указанном размере |
| formatted\_user.account\_type\_name | название типа аккаунта |
| formatted\_user.account\_type\_color | цвет типа аккаунта |
| formatted\_user.full\_background\_url | бэкграуд профайла |
| statistics.likes\_count | общее количество лайков |
| statistics.dislikes\_count | общее количество дислайков |
| statistics.rating\_count | =&quot;likes\_count&quot;-&quot;dislikes\_count&quot; |
| statistics.comments\_count | общее количество комментариев |
| statistics.purchase\_count | общее количество приобретений публикации(если pay=1) |
| statistics.repost\_count | общее количество репостов |
| statistics.views | общее количество просмотров |
| statistics.you\_liked | лайк по отношению к владельцу токена |
| statistics.you\_disliked | дислайк по отношению к владельцу токена |
| statistics.is\_favourite | является ли публикация избранной |
| statistics.you\_reposted | репост по отношению к владельцу токена  |
| statistics.you\_abused | жалоба по отношению к владельцу токена |
| statistics.visited | посещена ли публикация владельцем токена |
| statistics.paid | произведена ли оплата публикации владельцем токена |
| statistics.you\_pinned | закреплена ли публикация владельце токена |
| statistics.archived | заархивирована ли публикация владельцем токена |
| statistics.unique\_views | количество уникальных просмотров |
| subscription\_info.your\_post | принадлежность публикации владельцу токена  |
| subscription\_info.you\_followed | подписан ли пользователь на другие посты автора данного типа |
| post\_type\_object.id | id типа публикации |
| post\_type\_object.name | название типа публикации |
| post\_type\_object.parent\_type | показывает какой у данного типа публикаций тип родитель |
| excerpt | текст публикации (тут более точно нужно написать) |
| url\_slug | фронт url  публикации |
| url\_back\_slug | фронт урл для кнопки &quot;назад&quot; на странице открытой  публикации, если история браузера отсутствует |
| tags | массив тегов |
| is\_repost | является ли публикация репостом другой публикации |
| has\_more\_text | атрибут, говорящий, если дополнительный текст за excerpt текстом, специально созданный для фронта для отображения полного текста, скрытого в ленте |
| text | полный текст публикации |
| postable.id | id публикации именно внутри сборки |
| postable.category\_id | id категории блогов |
| postable.cards |   |
| postable.category.id | id категории блогов  |
| postable.category.name | ключ категории блогов |
| postable.top\_cards.value\_translation\_key | ключ категории для отображения открытой публикации   |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение 250px для сборок |
| postable.full\_image\_800\_url | ссылка на изображение в 800px для лент  |

<a name="news"></a>
## Новости

Формат Ответа

{
    "data": {
        "id": 30501,
        "conversation_id": 18872,
        "post_id": 30501,
        "post_type": "news",
        "title": "Обзор смарт-часов Lenovo E1",
        "language": {
            "id": 1,
            "native_name": "Русский",
            "code": "ru",
            "flag_icon_url": false
        },
        "pay": 0,
        "cost": 0,
        "user_id": 141,
        "access_type": 1,
        "comment_allow": 2,
        "formatted_created_date": "5 минут назад",
        "formatted_user": {
            "id": 141,
            "first_name": "Happycoin",
            "last_name": "⠀",
            "nickname": "Happycoin",
            "account_type": 0,
            "rank_name": "general",
            "rank_level": "amateur",
            "value": 1.8900000000000001,
            "stars": 1,
            "full_name": "Happycoin ⠀",
            "full_avatar_url": "https://dev.taklimakan.network/storage/avatars/141/CTpBNSvmXJHaQsfWmcfKjb3NyTxNyOf8SZiPE04b.jpg",
            "full_avatar_160_url": false,
            "account_type_name": null,
            "account_type_color": null,
            "full_background_url": false
        },
        "statistics": {
            "likes_count": 0,
            "dislikes_count": 0,
            "rating_count": 0,
            "comments_count": 0,
            "purchase_count": 0,
            "repost_count": 0,
            "views": 1,
            "you_liked": false,
            "you_disliked": false,
            "is_favourite": false,
            "you_reposted": false,
            "you_abused": false,
            "visited": true,
            "paid": false,
            "you_pinned": false,
            "archived": false,
            "unique_views": 1
        },
        "subscription_info": {
            "your_post": false,
            "you_followed": false
        },
        "post_type_object": {
            "id": 8,
            "name": "news",
            "parent_type": null
        },
        "excerpt": " \nПосле долгого отсутствия Lenovo снова вернулась на рынок со своими новыми ",
        "url_slug": "/news/30501",
        "url_back_slug": "/news",
        "tags": [
            {
                "id": 8709,
                "name": "Гаджеты"
            },
            {
                "id": 8713,
                "name": "Lenovo"
            },
            {
                "id": 11790,
                "name": "Смарт-Часы"
            }
        ],
        "is_repost": false,
        "has_more_text": true,
        "text": "hey guys",
        "postable": {
            "id": 32605,
            "excerpt": "После долгого отсутствия Lenovo снова вернулась на рынок со своими новыми смарт-часами Lenovo E1.",
            "source": "https://happycoin.club/obzor-smart-chasov-lenovo-e1/",
            "is_active": 1,
            "news_provider_id": 12,
            "formatted_news_date": "2 часа назад",
            "cards": [
                {
                    "translation_key": "open_publication_news_providers",
                    "values": [
                        "happycoin"
                    ]
                }
            ],
            "full_image_url": "https://dev.taklimakan.network/storage/images/news/201908/5d5c5110b3672.jpg",
            "full_image_250_url": "https://dev.taklimakan.network/storage/images/news/201908/5d5c5110b3672_250.jpg",
            "full_image_800_url": "https://dev.taklimakan.network/storage/images/news/201908/5d5c5110b3672_800.jpg"
        }
    }
}


| **Атрибут** | **Описание** |
| --- | --- |
| id  | id публикации |
| conversation\_id | id чата публикации |
| post\_id |  id публикации |
| post\_type | тип поста(зависит от сборки) |
| title | Название публикации |
| language.id | id языка публикации |
| language.native\_name | название языка на выбранном языке |
| language.code | краткий код языка |
| language.flag\_icon\_url | ссылка на иконку языка |
| pay | платный/бесплатный контент |
| cost | стоимость контента |
| user\_id | id пользователя |
| access\_type | тип доступа, указываемый при создании поста |
| comment\_allow | доступ к комментариям |
| formatted\_created\_date | время создания публкации |
| formatted\_user.id | id автора публикации |
| formatted\_user.first\_name | имя автора |
| formatted\_user.last\_name | фамилия автора |
| formatted\_user.nickname | никнейм автора |
| formatted\_user.account\_type | тип аккаунта автора |
| formatted\_user.rank\_name | ранг автора, к которому принадлежит публикация |
| formatted\_user.rank\_level | уровень ранга |
| formatted\_user.value | числовой уровень автора по выбранной(к которому принадлежит публикация) сборке |
| formatted\_user.stars | количество звезд автора в выбранном ранге |
| formatted\_user.full\_name | полное имя автора |
| formatted\_user.full\_avatar\_url | ссылка на аватар автора |
| formatted\_user.full\_avatar\_160\_url | ссылка на аватар автора в указанном размере |
| formatted\_user.account\_type\_name | название типа аккаунта |
| formatted\_user.account\_type\_color | цвет типа аккаунта |
| formatted\_user.full\_background\_url |   |
| statistics.likes\_count | общее количество лайков |
| statistics.dislikes\_count | общее количество дислайков |
| statistics.rating\_count | =&quot;likes\_count&quot;-&quot;dislikes\_count&quot; |
| statistics.comments\_count | общее количество комментариев |
| statistics.purchase\_count | общее количество приобретений публикации(если pay=1) |
| statistics.repost\_count | общее количество репостов |
| statistics.views | общее количество просмотров |
| statistics.you\_liked | лайк по отношению к владельцу токена |
| statistics.you\_disliked | дислайк по отношению к владельцу токена |
| statistics.is\_favourite | является ли публикация избранной |
| statistics.you\_reposted | репост по отношению к владельцу токена  |
| statistics.you\_abused | жалоба по отношению к владельцу токена |
| statistics.visited | посещена ли публикация владельцем токена |
| statistics.paid | оплата публикации по отношению к владельцу токена |
| statistics.you\_pinned |   |
| statistics.archived | заархивирована ли публикация по отношению владельцу токена |
| statistics.unique\_views | количество уникальных просмотров |
| subscription\_info.your\_post | принадлежность публикации владельцу токена  |
| subscription\_info.you\_followed |   |
| post\_type\_object.id | id типа публикации |
| post\_type\_object.name | название типа публикации |
| post\_type\_object.parent\_type |   |
| excerpt | текст публикации |
| url\_slug | путь до id публикации |
| url\_back\_slug | путь до типа публикации |
| tags | массив тегов |
| is\_repost |   |
| has\_more\_text | атрибут, специально созданный для фронта для отображения полного текста, скрытого в ленте |
| text | полный текст публикации |
| postable.id | id публикации именно внутри сборки |
| postable.excerpt | id категории публикации в сборке |
| postable.source | ссылка на источник  |
| postable.is\_active |   |
| postable.news\_provider\_id | порядковый id источника новости |
| postable.formatted\_news\_date | время добавления публикации(новости) |
| postable.cards.translation\_key | ключ типа публикации |
| postable.cards.values | значение источника публикации |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение в указанном размере |
| postable.full\_image\_800\_url | ссылка на изображение в указанном размере |


<a name="trading"></a>
## Трейдинг
Основное тело запроса идентично с остальными типами публикации. В зависимости от подкатегории Трейдингов меняется лишь объект “postable”

<a href="trading-signals"></a>
**Ответ для Торгового Сигнала**

"postable": {
            "id": 493,
            "position": "sale",
            "trade_type": "long",
            "exchange_id": null,
            "take_profit": "1",
            "stop_loss": "-1",
            "opening_price": "-1",
            "closing_price": "-2",
            "capital_percent": "-1",
            "market_pair_id": null,
            "full_image_url": false,
            "full_image_250_url": false,
            "full_image_800_url": false,
            "market_pair": null,
            "exchange": null,
            "cards": [
                {
                    "translation_key": "open_publication_market_pairs",
                    "values": [
                        "сryptopair_autocomplete_any"
                    ]
                },
                {
                    "translation_key": "open_publication_type_of_trade",
                    "value_translation_key": "editor_trade_signal_type_of_trade_long_term",
                    "values": [
                        "long"
                    ]
                },
                {
                    "translation_key": "open_publication_position",
                    "values": [
                        "trading_filter_position_sale"
                    ]
                },
                {
                    "translation_key": "open_publication_exchange",
                    "values": [
                        "cryptoexchange_autocomplete_any"
                    ]
                }
            ],
            "table": [
                {
                    "value": "-1",
                    "translation_key": "editor_position_opening_price"
                },
                {
                    "value": "-2",
                    "translation_key": "editor_position_closing_price"
                },
                {
                    "value": "-1",
                    "translation_key": "editor_capital_transaction"
                },
                {
                    "value": "1",
                    "translation_key": "editor_take_profit"
                },
                {
                    "value": "-1",
                    "translation_key": "editor_stop_loss"
                }
            ]
        }

| Атрибут | Описание |
| --- | --- |
| postable.id | id публикации именно внутри сборки |
| postable.position | Позиция публикации: покупка-продажа(доступна лишь для торговых сигналов) |
| postable.trade\_type | Тип торговли: долгосрочный и краткосрочный |
| postable.exchange\_id | id биржи |
| postable.take\_profit | Параметр, указываемый при создании торгового сигнала. |
| postable.stop\_loss | Параметр, указываемый при создании торгового сигнала. |
| postable.opening\_price | Параметр, указываемый при создании торгового сигнала. Цена открытия |
| postable.closing\_price | Параметр, указываемый при создании торгового сигнала. Цена открытия |
| postable.capital\_percent | Параметр, указываемый при создании торгового сигнала. Процент от капитала на сделку |
| postable.market\_pair\_id | id криптопары |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение в указанном размере |
| postable.full\_image\_800\_url | ссылка на изображение в указанном размере |
| postable.market\_pair | выбранная криптопара |
| postable.exchange | выбранная биржа |
| postable.cards.translation\_key | ключи, отвечающие за выбранные при создании параметры(криптопары, биржи, тип торговли, позиция) |
| postable.cards.value | значение ключа |
| postable.table.value | значения ключей |
| postable.table.translation\_key | ключи, предназначенные для параметров из текстового редактора |

<a href="trading-startegy"></a>
**Ответ для Торговой Стратегии**

"postable": {
            "id": 235,
            "take_profit": null,
            "stop_loss": null,
            "capital_percent": null,
            "time_interval_id": 10,
            "exchanges": [],
            "indicators": [
                {
                    "id": 2,
                    "name": "Кумулятивный индекс колебаний"
                }
            ],
            "types": [
                {
                    "id": 5,
                    "name": "Долгосрочный"
                },
                {
                    "id": 6,
                    "name": "Среднесрочный"
                }
            ],
            "market_pairs": [
                {
                    "id": 361,
                    "base": {
                        "id": 1,
                        "name": "Bitcoin",
                        "symbol": "BTC",
                        "slug": "bitcoin"
                    },
                    "quote": {
                        "id": 12,
                        "name": "Monero",
                        "symbol": "XMR",
                        "slug": "monero"
                    }
                }
            ],
            "time_interval": {
                "id": 10,
                "name": "1 год"
            },
            "cards": [
                {
                    "translation_key": "open_publication_category_strategy_type",
                    "values": [
                        "Долгосрочный",
                        "Среднесрочный"
                    ]
                },
                {
                    "translation_key": "open_publication_exchange",
                    "values": [
                        "cryptoexchange_autocomplete_any"
                    ]
                },
                {
                    "translation_key": "open_publication_indicatiors",
                    "values": [
                        "Кумулятивный индекс колебаний"
                    ]
                },
                {
                    "translation_key": "open_publication_time_interval",
                    "values": [
                        "1 год"
                    ]
                },
                {
                    "translation_key": "open_publication_market_pairs",
                    "values": [
                        "BTC/XMR"
                    ]
                }
            ],
            "table": [],
            "full_image_url": "https://dev.taklimakan.network/storage/508/2019/08/12/image/5d5175046c366.jpg",
            "full_image_250_url": "https://dev.taklimakan.network/storage/508/2019/08/12/image/5d5175046c366_250.jpg",
            "full_image_800_url": "https://dev.taklimakan.network/storage/508/2019/08/12/image/5d5175046c366_800.jpg"
        }


| Атрибут | Описание |
| --- | --- |
| postable.id | id публикации именно внутри сборки |
| postable.take\_profit | Параметр, указываемый при создании торгового сигнала. |
| postable.stop\_loss | Параметр, указываемый при создании торгового сигнала. |
| postable.capital\_percent | Параметр, указываемый при создании торгового сигнала. Процент от капитала на сделку |
| postable.time\_interval\_id | Параметр, указываемый при создании торгового сигнала.  |
| postable.exchanges.id | порядковый id биржи |
| postable.exchanges.name | название биржи |
| postable.indicators.id | порядковый id индикатора |
| postable.indicators.name | название индикатора |
| postable.type.id | пордяковый id типа торговой стратегии |
| postable.type.name | название типа торговой стратегии |
| postable.market\_pairs.id | порядковый номер криптопары |
| postable.market\_pairs.base.id | порядковый номер основной криптовалюты |
| postable.market\_pairs.base.name | название основной криптовалюты |
| postable.market\_pairs.base.symbol | обозначение криптовалюты |
| postable.market\_pairs.base.slug | слаг основной криптовалюты |
| postable.market\_pairs.quote.id | порядковый номер дополнительной криптовалюты |
| postable.market\_pairs.quote.name | название дополнительной криптовалюты |
| postable.market\_pairs.quote.symbol | обозначение дополнительный криптовалюты |
| postable.market\_pairs.quote.slug | слаг дополнительной криптовалюты |
| postable.time\_interval.id | порядковый номер интервала времени(параметр, выбираемый при создании публикации) |
| postable.time\_interval.name | название интервала времени |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение в указанном размере |
| postable.full\_image\_800\_url | ссылка на изображение в указанном размере |
| postable.cards.translation\_key | ключи, отвечающие за выбранные при создании параметры(криптопары, биржи, тип торговли, позиция) |
| postable.cards.value | значение ключа |
| postable.table.value | значения ключей |
| postable.table.translation\_key | ключи, предназначенные для параметров из текстового редактора |

<a href="trading-bot"></a>
**Ответ для Торгового Бота**

"postable": {
            "id": 171,
            "time_interval_id": 10,
            "take_profit": 0,
            "stop_loss": 0,
            "bot": null,
            "income": null,
            "startup_capital": null,
            "drawdown_level": null,
            "full_bot_url": false,
            "exchanges": [],
            "strategy_types": [],
            "market_pairs": [
                {
                    "id": 18700,
                    "base": {
                        "id": 1441,
                        "name": "FantasyGold",
                        "symbol": "FGC",
                        "slug": "fantasygold"
                    },
                    "quote": {
                        "id": 22,
                        "name": "Dogecoin",
                        "symbol": "DOGE",
                        "slug": "dogecoin"
                    }
                }
            ],
            "time_interval": {
                "id": 10,
                "name": "1 год"
            },
            "cards": [
                {
                    "translation_key": "open_publication_exchange",
                    "values": [
                        "cryptoexchange_autocomplete_any"
                    ]
                },
                {
                    "translation_key": "open_publication_time_interval",
                    "values": [
                        "1 год"
                    ]
                },
                {
                    "translation_key": "open_publication_market_pairs",
                    "values": [
                        "FGC/DOGE"
                    ]
                }
            ],
            "table": [
                {
                    "value": 0,
                    "translation_key": "editor_take_profit",
                    "value_translation_key": "openpost_trading_bot_takeprofit_no"
                },
                {
                    "value": 0,
                    "translation_key": "editor_stop_loss",
                    "value_translation_key": "openpost_trading_bot_stoploss_no"
                }
            ],
            "bot_info": {
                "full_name": "",
                "name": "",
                "ext": ""
            },
            "full_image_url": "https://dev.taklimakan.network/storage/209/2019/08/09/image/5d4d40c104d21.jpg",
            "full_image_250_url": "https://dev.taklimakan.network/storage/209/2019/08/09/image/5d4d40c104d21_250.jpg",
            "full_image_800_url": "https://dev.taklimakan.network/storage/209/2019/08/09/image/5d4d40c104d21_800.jpg"
        }


| Атрибут | Описание |
| --- | --- |
| postable.id | id публикации именно внутри сборки |
| postable.take\_profit | Параметр, указываемый при создании торгового сигнала. |
| postable.stop\_loss | Параметр, указываемый при создании торгового сигнала. |
| postable.time\_interval\_id | Параметр, указываемый при создании торгового сигнала.  |
| postable.bot | ссылка на прикрепленный файл(изображение) |
| postable.income | Доходность. Указывается при создании публикации. |
| postable.startup\_capital | стартовый капитал. Указывается при создании публикации. |
| postable.drawdown\_level | уровень просадки. Указывается при создании публикации. |
| postable.full\_bot\_url | ссылка на изображение бота из локального хранилища dev.taklimakan |
| postable.exchanges.id | порядковый id биржи |
| postable.exchanges.name | название биржи |
| postable.strategy\_types | массив типов стратегий |
| postable.indicators.id | порядковый id индикатора |
| postable.indicators.name | название индикатора |
| postable.type.id | пордяковый id типа торговой стратегии |
| postable.type.name | название типа торговой стратегии |
| postable.market\_pairs.id | порядковый номер криптопары |
| postable.market\_pairs.base.id | порядковый номер основной криптовалюты |
| postable.market\_pairs.base.name | название основной криптовалюты |
| postable.market\_pairs.base.symbol | обозначение криптовалюты |
| postable.market\_pairs.base.slug | слаг основной криптовалюты |
| postable.market\_pairs.quote.id | порядковый номер дополнительной криптовалюты |
| postable.market\_pairs.quote.name | название дополнительной криптовалюты |
| postable.market\_pairs.quote.symbol | обозначение дополнительный криптовалюты |
| postable.market\_pairs.quote.slug | слаг дополнительной криптовалюты |
| postable.time\_interval.id | порядковый номер интервала времени(параметр, выбираемый при создании публикации) |
| postable.time\_interval.name | название интервала времени |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение в указанном размере |
| postable.full\_image\_800\_url | ссылка на изображение в указанном размере |
| postable.cards.translation\_key | ключи, отвечающие за выбранные при создании параметры(криптопары, биржи, тип торговли, позиция) |
| postable.cards.value | значение ключа |
| postable.table.value | значения ключей |
| postable.table.translation\_key | ключи, предназначенные для параметров из текстового редактора |


<a href="education"></a>
## Образование

**Ответ для Образования**

{
    "data": {
        "id": 29361,
        "conversation_id": 17663,
        "post_id": 29361,
        "post_type": "course",
        "title": "Сказка Белоснежка и семь гномов",
        "language": {
            "id": 1,
            "native_name": "Русский",
            "code": "ru",
            "flag_icon_url": false
        },
        "pay": 0,
        "cost": 0,
        "user_id": 209,
        "access_type": 1,
        "comment_allow": 2,
        "formatted_created_date": " 8 авг 2019 15:16",
        "formatted_user": {
            "id": 209,
            "first_name": "Dana",
            "last_name": "Sultan",
            "nickname": "Nika",
            "account_type": 0,
            "rank_name": "mentor",
            "rank_level": "amateur",
            "value": 42.96,
            "stars": 1,
            "full_name": "Dana Sultan",
            "full_avatar_url": "https://dev.taklimakan.network/storage/avatars/209/5c98952384597.jpg",
            "full_avatar_160_url": false,
            "account_type_name": null,
            "account_type_color": null,
            "full_background_url": false
        },
        "statistics": {
            "likes_count": 8,
            "dislikes_count": 3,
            "rating_count": 5,
            "comments_count": 0,
            "purchase_count": 0,
            "repost_count": 0,
            "views": 1,
            "you_liked": true,
            "you_disliked": false,
            "is_favourite": false,
            "you_reposted": false,
            "you_abused": false,
            "visited": true,
            "paid": false,
            "you_pinned": false,
            "archived": false,
            "unique_views": 1
        },
        "subscription_info": {
            "your_post": false,
            "you_followed": true
        },
        "post_type_object": {
            "id": 6,
            "name": "course",
            "parent_type": {
                "id": 5,
                "name": "education",
                "parent_type": null
            }
        },
        "excerpt": "Было то в середине зимы, падали снежинки, точно пух с неба, и сидела королева у окошка, — рама его была из черного дерева,",
        "url_slug": "/education/easy/course/29361",
        "url_back_slug": "/education",
        "tags": [],
        "is_repost": false,
        "has_more_text": true,
        "text": "<span style=\"font-size:1rem;font-weight:400;\">Было то в середине зимы, падали снежинки, точно пух с неба, и сидела королева у окошка</p>",
        "postable": {
            "id": 577,
            "level": "easy",
            "subject_id": 7,
            "formatted_lectures": [],
            "formatted_subject": {
                "id": 7,
                "name": "education_category_tutorial"
            },
            "top_cards": [
                {
                    "value_translation_key": "education_category_tutorial"
                }
            ],
            "full_image_url": "https://dev.taklimakan.network/storage/209/2019/08/08/image/5d4be8525136a.gif",
            "full_image_250_url": "https://dev.taklimakan.network/storage/209/2019/08/08/image/5d4be8525136a_250.gif",
            "full_image_800_url": "https://dev.taklimakan.network/storage/209/2019/08/08/image/5d4be8525136a_800.gif"
        }
    }
}

| Атрибут | Описание |
| --- | --- |
| id  | id публикации |
| conversation\_id | id чата публикации |
| post\_id |  id публикации |
| post\_type | тип поста(зависит от сборки)(lecture/course) |
| title | Название публикации |
| language.id | id языка публикации |
| language.native\_name | название языка на выбранном языке |
| language.code | краткий код языка |
| language.flag\_icon\_url | ссылка на иконку языка |
| pay | платный/бесплатный контент |
| cost | стоимость контента |
| user\_id | id пользователя |
| access\_type | тип доступа, указываемый при создании поста |
| comment\_allow | доступ к комментариям |
| formatted\_created\_date | время создания публкации |
| formatted\_user.id | id автора публикации |
| formatted\_user.first\_name | имя автора |
| formatted\_user.last\_name | фамилия автора |
| formatted\_user.nickname | никнейм автора |
| formatted\_user.account\_type | тип аккаунта автора |
| formatted\_user.rank\_name | ранг автора, к которому принадлежит публикация |
| formatted\_user.rank\_level | уровень ранга |
| formatted\_user.value | числовой уровень автора по выбранной(к которому принадлежит публикация) сборке |
| formatted\_user.stars | количество звезд автора в выбранном ранге |
| formatted\_user.full\_name | полное имя автора |
| formatted\_user.full\_avatar\_url | ссылка на аватар автора |
| formatted\_user.full\_avatar\_160\_url | ссылка на аватар автора в указанном размере |
| formatted\_user.account\_type\_name | название типа аккаунта |
| formatted\_user.account\_type\_color | цвет типа аккаунта |
| formatted\_user.full\_background\_url |   |
| statistics.likes\_count | общее количество лайков |
| statistics.dislikes\_count | общее количество дислайков |
| statistics.rating\_count | =&quot;likes\_count&quot;-&quot;dislikes\_count&quot; |
| statistics.comments\_count | общее количество комментариев |
| statistics.purchase\_count | общее количество приобретений публикации(если pay=1) |
| statistics.repost\_count | общее количество репостов |
| statistics.views | общее количество просмотров |
| statistics.you\_liked | лайк по отношению к владельцу токена |
| statistics.you\_disliked | дислайк по отношению к владельцу токена |
| statistics.is\_favourite | является ли публикация избранной |
| statistics.you\_reposted | репост по отношению к владельцу токена  |
| statistics.you\_abused | жалоба по отношению к владельцу токена |
| statistics.visited | посещена ли публикация владельцем токена |
| statistics.paid | оплата публикации по отношению к владельцу токена |
| statistics.you\_pinned |   |
| statistics.archived | заархивирована ли публикация по отношению владельцу токена |
| statistics.unique\_views | количество уникальных просмотров |
| subscription\_info.your\_post | принадлежность публикации владельцу токена  |
| subscription\_info.you\_followed |   |
| post\_type\_object.id | id типа публикации |
| post\_type\_object.name | название типа публикации |
| post\_type\_object.parent\_type |   |
| excerpt | текст публикации |
| url\_slug | путь до id публикации |
| url\_back\_slug | путь до типа публикации |
| tags | массив тегов |
| is\_repost |   |
| has\_more\_text | атрибут, специально созданный для фронта для отображения полного текста, скрытого в ленте |
| text | полный текст публикации |
| postable.id | id публикации именно внутри сборки |
| postable.level | уровень курса/лекции |
| postable.subject\_id | порядковый номер категории курса |
| postable.formatted\_lectures | массив лекций, входящих в курс |
| postable.formatted\_subject.id | порядковый номер категории курса |
| postable.formatted\_subject.name | название категории курса |
| postable.top\_cards.value\_translation\_key | ключ типа публикации |
| postable.full\_image\_url | ссылка на полное изображение публикации |
| postable.full\_image\_250\_url | ссылка на изображение в указанном размере |
| postable.full\_image\_800\_url | ссылка на изображение в указанном размере |

