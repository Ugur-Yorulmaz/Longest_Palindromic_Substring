# 5. Longest Palindromic Substring
import time
# s = "babad"
# s="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
# s="eabcb"
# s="klebreabcbaerjlkas"
# s="a"
s="wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"
# çözüm="knnk"
# s="vyzonecajxxdvswhftixmzgjbfoeilbnchqmdgoxfmkkkkcqguavfozmplhzgothrwpukzgkctdacbxefrzrmbgwwrrhpcvqwvgwgknyrtxxoligsqpbqoucltakbkywwssyodzydsjxeuvgiqqitkfkqnxsfflgbjvbxdrworsdkowtkgabnszgsmgytupybdclmmsmougfendwvzarfdfbixjnlxvevqfoohcgrrysofifdfulygrmkwpimduzzluojeqixdtcxhcqnfsdbunmhsglhiplgbhrqrrrprffjfradvbifxxhoqylkejyprxdtianietnjumltxywfowopghurofvwtxvaxtqnjbzwvljjwfmmlhixogwwyaoysvrpgfymyqjschhqcwvytkreirdxfapaomayebhkzxgmlthoxialmtnilfopvhhqlocytyrtpfmpgqakdbrsteurcpfvruicuxzukfpwjwgnuaaungwjwpfkuzxuciurvfpcruetsrbdkaqgpmfptrytycolqhhvpoflintmlaixohtlmgxzkhbeyamoapafxdrierktyvwcqhhcsjqymyfgprvsyoaywwgoxihlmmfwjjlvwzbjnqtxavxtwvforuhgpowofwyxtlmujnteinaitdxrpyjeklyqohxxfibvdarfjffrprrrqrhbglpihlgshmnubdsfnqchxctdxiqejoulzzudmipwkmrgylufdfifosyrrgchoofqvevxlnjxibfdfrazvwdnefguomsmmlcdbyputygmsgzsnbagktwokdsrowrdxbvjbglffsxnqkfktiqqigvuexjsdyzdoysswwykbkatlcuoqbpqsgiloxxtrynkgwgvwqvcphrrwwgbmrzrfexbcadtckgzkupwrhtogzhlpmzofvaugqckkkkmfxogdmqhcnblieofbjgzmxitfhwsvdxxjacenozyv"
# s="fjnfkfbfeuujctmyttwidcrdjtkfoaylsceqqzzmkpyvljkwcxxtmxiwkrgoahxztuppnvxhyionhpakvjoizdzcqxuyaidjadrhfhuhbncijokbthvuigjytipgygnonhgkpvsqimxpslmptieumhunjlafttjstaxnivrpqcxrgocvaicpwfnmtkgbjnbfopxaiduqihomrdmhzzyzddytiqdjzmmqwmeyoqnttmiujobihdifkbntpphjhgxzbjpulnokvceohloltyosddbopgkllcxzzkfzmkywxlpkdjlorgorxzownuajjzcxuhyqexfklssbtralzlvdbtxapccipvvgjtusfsanvnyehpkwirygqogtsicwycgnajwekuzffhlsvfgqwpbuinwhvpqxjhamhxayicchmxmurakhzhoghnupohaqanduhjkegggpyetwebcjgavpspfjaoakjkktaxwehpyqvsczhbbhzcsvqyphewxatkkjkaoajfpspvagjcbewteypgggekjhudnaqahopunhgohzhkarumxmhcciyaxhmahjxqpvhwniubpwqgfvslhffzukewjangcywcistgoqgyriwkpheynvnasfsutjgvvpiccpaxtbdvlzlartbsslkfxeqyhuxczjjaunwozxrogroljdkplxwykmzfkzzxcllkgpobddsoytlolhoecvkonlupjbzxghjhpptnbkfidhibojuimttnqoyemwqmmzjdqityddzyzzhmdrmohiqudiaxpofbnjbgktmnfwpciavcogrxcqprvinxatsjttfaljnuhmueitpmlspxmiqsvpkghnongygpityjgiuvhtbkojicnbhuhfhrdajdiayuxqczdziojvkaphnoiyhxvnpputzxhaogrkwixmtxxcwkjlvypkmzzqqecslyaofktjdrcdiwttymtcjuuefbfkfnjf"

# s="a"
tic=time.time()
# print(len(s))
res=s[0]
l=0
r=len(s)-1
# print(l,r)
# print("dizi   :",s[l:r+1])
while r>l:
    if len(res)>len (s[l:r]):
        break
    # print("DİZİİİİİ   :", s[l:r + 1])
    for i in range(len(s)-1,l,-1):
        # print("i:",i)
        # print("sol,sağ 1",s[l],s[i])
        if s[l]==s[i]:
            a=s[l:i+1]
            if a==a[::-1]:
                if len(a)>len(res):
                    res=a
                    # time.sleep(3)
                    # print("res    :",res)
    l=l+1

    for j in range(r):
        # print("j:",j)
        # print("sol,sağ 2",s[j],s[r])
        if s[j]==s[r]:
            b=s[j:r+1]
            # print(b)
            if b==b[::-1]:
                if len(b)>len(res):
                    res=b
                    # time.sleep(3)

                    # print("res",res)
    r=r-1

toc=time.time()
print("Süre     :",toc-tic)
print("Final   :",res)
print(len(res))


