from lib.User import User
import binascii
obj=User()
print(obj.add(name="Rahul Hassan",nId="128646979",description="New member",level=3,char="0"))
#print(obj.verify())
#objNFT=NFT()

#privateKey="2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949435841494241414b426751433141526638497070727565386f647271624a557048334951705974526d35456f6c324c6964686c6f6c51487764517830710a567372716241393136456d79355148426873512b305a31465166474c584c5a64477048316b3051763046536d4a70517435313862524f494c36462b425a4e72680a324a4742363164785a56505a783273647a56334d307a45724e414d4b6a4f4c68674e4f424f5961676f3751776d7a564d794341616d78453564774944415141420a416f474141676f72476131443644444872594d436c5576666372544e6d417378714d326e2f336137416c6b6737496c734664686b71682f5476306e57487252330a3875364d32507735393656672b654f59776d3243376a6b57576c7a2b5438623259726c4c6958397761464d674d305032474c337a7364527a5a396a376b6e31740a2f686d78394e7a2f575145696b5432463871737259315253374c622f5048572f4b766479584d56336a587135777555435151445436476d43534656774c6359610a7978706f6c7237624f4a58626d7249706346572b526e3746724971364e7a6772374c6a6f75764567527a756965316d6a472b37755163484c3441382f6c4735660a746f5147514e4839416b45413271714f542f7a496b6447453365314b6735676e71303148577a3055512b7753496853614a6135614643786f69612f706d6467740a744249676b31764a6e637533494a2b73446e71696d3471384550415278576c7067774a414c39344d4631586e6c744f414d4955346a652b665a54322b2f4542520a686e4c4e7135475a43575955594551672b43736443645651716f337374714e4f65443354467862626841593036355048367537376d37344173514a415254466e0a4b775277613051446154356e4c39443737496264703439695645506c555164333536694f4e49674135474458364b697866614f6d7a7a70695342356f616c68630a56354353312b6c457259397038432f3142514a42414e4a68494646395a6e50687958736f56524459645a5774744c7456625977542f686d2f3750457a3976544d0a356b437a7a385643726853526637327361756d614e334b5170334a4451547a73653532686178487964366b3d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d"
nft="603c12257afa281384267d9af9ea57299d3e9d5e30dc4c6ed6b339e188d7db0d"
fileLocation="""https://drive.google.com/file/d/1mMLCgAOTddto82KTevoWjHu6EzjdtsFP/view?usp=drivesdk"""
level=3
char="0"

#objNFT.add_nft(privateKey=privateKey,nft=nft,fileLocation=fileLocation,level=level,char=char)
#


#print(objNFT.findOwner(nft=nft))

#sellerPublicKey="2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435371475349623344514542415155414134474e4144434269514b426751433141526638497070727565386f647271624a557048334951700a5974526d35456f6c324c6964686c6f6c5148776451783071567372716241393136456d79355148426873512b305a31465166474c584c5a64477048316b3051760a3046536d4a70517435313862524f494c36462b425a4e7268324a4742363164785a56505a783273647a56334d307a45724e414d4b6a4f4c68674e4f424f5961670a6f3751776d7a564d794341616d78453564774944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d"

#buyerPublicKey="2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435371475349623344514542415155414134474e4144434269514b42675143743255524f676d73764c4958776162424e44677058632b74630a46456771436f3843366d564f6d6b454e71357275474a2b346d31796475503948772b666d572f765632753630707277794c7a6d2f674a3067412f56664d42384d0a676e7a37446873486f365239594c48624b31534342725862684a5a434a3374686b52693532326e396175533452436d474a6f3430446b7a32705a63694a3747700a573051397058546767417338482f624642514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d"

#signature="42ac0cfec6b20078d0adb665479ed13ac85e1620fae5c24114e89c4858b477504095ad9a71d112e5fddafc3e2da8f0f5fa008cef3ad4aa4a30541d04502e5029c7dc1712c7529a56f051fa4524e79b8b030ce2e64f74d87b37216665dd2c0988ec1597096a5e5510879a4c11342b4e9ea70e941c8b9313b321b1a169b9da4beb"

#print(objNFT.check_signature(sellerPublicKey=sellerPublicKey,signature=signature))

#print(obj.transfer_nft(sellerPrivateKey="2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949435841494241414b426751433141526638497070727565386f647271624a557048334951705974526d35456f6c324c6964686c6f6c51487764517830710a567372716241393136456d79355148426873512b305a31465166474c584c5a64477048316b3051763046536d4a70517435313862524f494c36462b425a4e72680a324a4742363164785a56505a783273647a56334d307a45724e414d4b6a4f4c68674e4f424f5961676f3751776d7a564d794341616d78453564774944415141420a416f474141676f72476131443644444872594d436c5576666372544e6d417378714d326e2f336137416c6b6737496c734664686b71682f5476306e57487252330a3875364d32507735393656672b654f59776d3243376a6b57576c7a2b5438623259726c4c6958397761464d674d305032474c337a7364527a5a396a376b6e31740a2f686d78394e7a2f575145696b5432463871737259315253374c622f5048572f4b766479584d56336a587135777555435151445436476d43534656774c6359610a7978706f6c7237624f4a58626d7249706346572b526e3746724971364e7a6772374c6a6f75764567527a756965316d6a472b37755163484c3441382f6c4735660a746f5147514e4839416b45413271714f542f7a496b6447453365314b6735676e71303148577a3055512b7753496853614a6135614643786f69612f706d6467740a744249676b31764a6e637533494a2b73446e71696d3471384550415278576c7067774a414c39344d4631586e6c744f414d4955346a652b665a54322b2f4542520a686e4c4e7135475a43575955594551672b43736443645651716f337374714e4f65443354467862626841593036355048367537376d37344173514a415254466e0a4b775277613051446154356e4c39443737496264703439695645506c555164333536694f4e49674135474458364b697866614f6d7a7a70695342356f616c68630a56354353312b6c457259397038432f3142514a42414e4a68494646395a6e50687958736f56524459645a5774744c7456625977542f686d2f3750457a3976544d0a356b437a7a385643726853526637327361756d614e334b5170334a4451547a73653532686178487964366b3d0a2d2d2d2d2d454e44205253412050524956415445204b45592d2d2d2d2d",buyerPublicKey="2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435371475349623344514542415155414134474e4144434269514b42675143743255524f676d73764c4958776162424e44677058632b74630a46456771436f3843366d564f6d6b454e71357275474a2b346d31796475503948772b666d572f765632753630707277794c7a6d2f674a3067412f56664d42384d0a676e7a37446873486f365239594c48624b31534342725862684a5a434a3374686b52693532326e396175533452436d474a6f3430446b7a32705a63694a3747700a573051397058546767417338482f624642514944415141420a2d2d2d2d2d454e44205055424c4943204b45592d2d2d2d2d",nft="889889"))

#buyer2=obj.findOwner(token="889889")
#print(buyer2)
#print(buyer1["buyer_public_key"]==buyer2["buyer_public_key"])