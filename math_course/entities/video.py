from dataclasses import dataclass


@dataclass
class Button:
    """Button entity."""
    text: str
    url: str | None = None
    callback_data: str | None = None


@dataclass
class Video:
    """Video entity."""
    urls: list[str]
    button: Button


VIDEOS = [
    Video(
        urls=[
            "https://rutube.ru/video/private/82dca29e86134c8828af6ad7b3b2e2c9/?p=ML688qlPUjaVmnCQLuGEIQ",
            "https://rutube.ru/video/private/b2e25e381f37b6db9b8c6e5e326be608/?p=ToBQHjzLWCEI91fT-9NaFw",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="first-lesson-done",
        ),
    ),
    Video(
        urls=[
            "https://rutube.ru/video/private/1ac2e2a39b319b3586ac52b1a34b6988/?p=9Dr7baYCAg8_aAIvh3MHLA",
            "https://rutube.ru/video/private/d0f4275a12bc25fc9952cf76dca57359/?p=VzhbQVQgPjJ-cbc6_ui3jw",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="second-lesson-done",
        ),
    ),
    Video(
        urls=[
            "https://rutube.ru/video/private/2bb2cde18479bf8e94e54b2305fce3a1/?p=n8Dm8aguYjS_koiq4T94Aw",
            "https://rutube.ru/video/private/05377a8ad5512c0f89e8a07277f03209/?p=UQUHIjuYGI_MwcZdMBcOSQ",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="third-lesson-done",
        ),
    ),
    Video(
        urls=[
            "https://rutube.ru/video/private/7440d9c1d720cf78c75ced06487bac37/?p=7ChGY9ZT45FVw-4X0cwCtQ",
            "https://rutube.ru/video/private/85fb64a9c17bb23ab6d9476c3c1fad55/?p=CqzukGo9FAv2R4SjUUs7fg",
            "https://rutube.ru/video/private/cec3a9028457738d8a1367043cfe14a6/?p=siMmPq9oiKzjtknI0im-5w",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="fifth-lesson-done",
        ),
    ),
    Video(
        urls=[
            "https://rutube.ru/video/private/21aa33b5a4169264b618ccd0fc66da3d/?p=Rhmv8a-LDEy7EvpLw1Ts7A",
            "https://rutube.ru/video/private/3e48b84f19188aad2273c231be196f6e/?p=OVpwKEmOZeBKdNz5EiyJZA",
            "https://rutube.ru/video/private/969bf08950f87b6492d7413c447aadb7/?p=YNyPrPC4w9ITc6WBmUM-Gg",
            "https://rutube.ru/video/private/96fdce31e98457f241004d31b9a506eb/?p=kGFcmahdFie_nx72jMjrng",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="sixth-lesson-done",
        ),
    ),
    Video(
        urls=[
            "https://rutube.ru/video/private/661443732ba8e80a507afb46b4bfdf2b/?p=OD5bFf_jTxANfJzDa7xHpg",
            "https://rutube.ru/video/private/8a473a380ac582f8c8314f55b093a931/?p=JkK4K-JiYNHYAemJJYm6vg",
        ],
        button=Button(
            text="✅ Я посмотрел",
            callback_data="seventh-lesson-done",
        ),
    )
]
