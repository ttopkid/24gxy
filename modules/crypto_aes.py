import logging
from hashlib import md5
from packages.aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding

logging.basicConfig(
    format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %I:%M:%S",
)
logger = logging.getLogger("ToolModule")


def create_sign(*args) -> str:
    """生成签名。

    该方法接收任意数量的参数, 将它们连接成一个字符串, 并附加一个预定义的密钥后,
    生成并返回该字符串的MD5签名。

    :param args: 要生成签名的参数。
    :type args: str

    :return: 生成的MD5签名。
    :rtype: str
    """
    sign_str = "".join(args) + "3478cbbc33f84bd00d75d7dfa69e0daa"
    return md5(sign_str.encode("utf-8")).hexdigest()


def aes_encrypt(
    plaintext: str, key: str = "23DbtQHR2UMbH6mJ", out_format: str = "hex"
) -> str:
    """AES加密。

    该方法使用指定的密钥对给定的明文字符串进行AES加密, 并返回加密后的密文。

    :param plaintext: 明文字符串。
    :type plaintext: str
    :param key: AES密钥, 默认 "23DbtQHR2UMbH6mJ"。
    :type key: str
    :param out_format: 输出格式, 默认 "hex"。
    :type out_format: str

    :return: 加密后的密文。
    :rtype: str

    :raises ValueError: 如果加密失败, 抛出包含详细错误信息的异常。
    """
    try:
        cipher = AESECBPKCS5Padding(key, out_format)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext
    except Exception as e:
        logger.error(f"加密失败: {e}")
        raise ValueError(f"加密失败: {str(e)}")


def aes_decrypt(
    ciphertext: str, key: str = "23DbtQHR2UMbH6mJ", out_format: str = "hex"
) -> str:
    """AES解密。

    该方法使用指定的密钥对给定的密文字符串进行AES解密, 并返回解密后的明文。

    :param ciphertext: 密文字符串。
    :type ciphertext: str
    :param key: AES密钥, 默认 "23DbtQHR2UMbH6mJ"。
    :type key: str
    :param out_format: 输出格式, 默认 "hex"。
    :type out_format: str

    :return: 解密后的明文。
    :rtype: str

    :raises ValueError: 如果解密失败, 抛出包含详细错误信息的异常。
    """
    try:
        cipher = AESECBPKCS5Padding(key, out_format)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext
    except Exception as e:
        logger.error(f"解密失败: {e}")
        raise ValueError(f"解密失败: {str(e)}")
