import os
import log_test.logUtils


def test():
    pass


log = log_test.logUtils.Logger(file_name='info.log', level='debug').log


if __name__ == '__main__':
    test()
    log.info(os.getcwd())
    log.debug(os.access(path='C:\\Users\\lisongtao\\PycharmProjects\\local-llst\\file_test', mode=os.F_OK))
    file = open(file='C:\\Users\\lisongtao\\Desktop\\ab.txt', mode='r', encoding='utf8')
    log.info(file)
    log.info(file.read())
    file.close()
    # with open(file='C:\\Users\\lisongtao\\Desktop\\ab.txt', mode='a', encoding='utf8') as file:
    #     file.write('\n天下皆知美之为美，恶矣；天下皆知善之为善，斯不善矣。有无相生，难易相成，长短相形，高下相盈，音声相和，先后相随,恒也。'
    #                '\n是以圣人处无为之事，行不言之教。万物作焉而不辞，生而不有，为而不恃，功成而弗居。夫唯弗居，是以不去。')

